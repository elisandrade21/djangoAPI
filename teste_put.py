import requests

url_notification = ('http://localhost:8000/api/v1/notifications/')

notification_atualizada = {
    "send_status": "Error",
    "comunication_type": "Sms",
    "send_data": "2020-12-15T15:10:02-03:00",
    "title": "Compra Efetuada",
    "body": "dfjsnnnnk",
    "receiver": "elisa@gmail.com",
    "name_receiver": "Elisa"
}

result = requests.put(url=f'{url_notification}7/',data=notification_atualizada)

# Testando o código de status HTTP
assert result.status_code == 200
print(result.status_code)


# Verificando se a notification com id 7 foi alterada 
notification = requests.get('http://localhost:8000/api/v1/notifications/7/')
print(notification.json())
