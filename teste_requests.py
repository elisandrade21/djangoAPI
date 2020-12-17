import requests

# REALIZANDO TESTES COM REQUESTS 

# Testando uma notificação pelo ID 

notifications = requests.get('http://localhost:8000/api/v1/notifications/7/')

# Testando uma notificação pelo Status

notifications_status = requests.get('http://localhost:8000/api/v1/notifications/Sent/')


# Acessando o código de status HTTP
print(notifications.status_code)

# Acessando o código de stattus HTTP do get pelo status 

print(notifications.status_code)


# Acessando os dados das respostas 

print(notifications.json())

# Retornar um dict com resultados 
print(type(notifications.json()))

# Acessando os registros nesse caso id  
print(notifications.json()['id'])

# Acessando os registros nesse caso name_receiver 
print(notifications.json()['name_receiver'])
  
# GET para retornar Notificações 
#notifications_all = requests.get('http://localhost:8000/api/v1/notifications/')
#print(notifications_all.status_code)
#print(notifications_all.json())