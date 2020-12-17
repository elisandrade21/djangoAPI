import requests

url_notification = ('http://localhost:8000/api/v1/notifications/')

#Remover uma notificação de id 9 
results = requests.delete(url=f'{url_notification}15/')

#Testando o código HTTP 
assert results.status_code == 204
print(results.status_code)


# Testando se o tamanho do conteúdo dp retorno é 0
assert len(results.text) == 0