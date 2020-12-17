import requests
# Testando uma notificação pelo ID 7 

notification = requests.get('http://localhost:8000/api/v1/notifications/7/')
print(notification.json())


# Testando se o endpoint está correto 
assert notification.status_code == 200
print(notification.status_code)


# Testando uma notificação pelo Status Error  

notification_status_error = requests.get('http://localhost:8000/api/v1/notifications/error/')
print(notification_status_error.json())

# Testando se o endpoint de listar pelo status = Error está correto 
assert notification_status_error.status_code == 200
print(notification_status_error.status_code)


# Testando uma notificação pelo Status Sent  

notification_status_sent = requests.get('http://localhost:8000/api/v1/notifications/sent/')
print(notification_status_sent.json())

# Testando se o endpoint de listar pelo status = Sent está correto 
assert notification_status_sent.status_code == 200
print(notification_status_sent.status_code)


# Testando uma notificação pelo Status Waiting

notification_status_waiting = requests.get('http://localhost:8000/api/v1/notifications/waiting/')
print(notification_status_waiting.json())

# Testando se o endpoint de listar pelo status = Waiting está correto 
assert notification_status_waiting.status_code == 200
print(notification_status_waiting.status_code)


# Testando se a notificação com ID 7 
assert notification.json()['title'] == 'Compra Efetuada'