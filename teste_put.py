import requests

url_notification = ('http://localhost:8000/api/v1/notifications/7/')

notification_atualizada = {
  "send_status": "Sent",
  "comunication_type": "Sms",
  "send_data": "2020-12-15T15:10:02-03:00",
  "title": "Pagamento Efetuado",
  "body": "Pode comemorar, seu pagamento foi confirmado!",
  "receiver": "8399973737",
  "name_receiver": "Elisa"
}

# Verificando 

result = requests.put(url=f'{url_notification}7/',data=notification_atualizada)
