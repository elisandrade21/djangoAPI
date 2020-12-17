import requests
import jsonpath

notifications = requests.get('http://localhost:8000/api/v1/notifications/10/')

resultados = jsonpath.jsonpath(notifications.json(),'results[0].name_receiver')
print(resultados)

name_receiver = jsonpath.jsonpath(notifications.json(),'results.name_receiver')
print(name_receiver)

# first_notifications = jsonpath.jsonpath(notifications.json(), 'results[0]')

# print(first_notifications)

# Primeiro destinatário
# nome = jsonpath.jsonpath(notifications.json(), 'results[0].nome')

# print(nome)

# nota_data = jsonpath.jsonpath(notifications.json(), 'results[0].avaliacao')

# print(nota_data)

# Todos os nomes de destinatários
# name = jsonpath.jsonpath(notifications.json(), 'results[*].name_receiver')
#print(nomes)


