import requests
"""
# Testando uma notificação pelo ID 7 

notification = requests.get('http://localhost:8000/api/v1/notifications/7/')
print(notification.json())

# Testando se o endpoint está correto 
assert notification.status_code == 200
print(notification.status_code)
"""
# Testando uma notificação pelo Status Error  

notification_status_error = requests.get('http://localhost:8000/api/v1/notifications/error/')
print(notification_status_error.json())

# Testando se o endpoint de listar pelo status = Error está correto 
assert notification_status_error.status_code == 200
