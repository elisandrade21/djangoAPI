import requests

url_notification = ('http://localhost:8000/api/v1/notifications/')
"""
# Testando o método POST 
# Notification 1 
new_notification1 = {
  "send_status": "Sent",
  "comunication_type": "Sms",
  "send_data": "2020-12-15T15:10:02-03:00",
  "title": "Pagamento Efetuado",
  "body": "Pode comemorar, seu pagamento foi confirmado!",
  "receiver": "8399973737",
  "name_receiver": "Elisa"
}
result = requests.post(url=url_notification,data=new_notification1)

#Testando o código de status HTTP 201
assert result.status_code == 201
print(result.status_code)

"""
# Testando o método POST 
# Notification 2
new_notification2 = {
  "send_status": "Error",
  "comunication_type": "Email",
  "send_data": "2020-12-15T15:10:02-03:00",
  "title": "Pagamento Não Foi Efetuado",
  "body": "Seu pagamento não foi confirmado!",
  "receiver": "elisandradecc@gmail.com",
  "name_receiver": "Elisa"
}
result2 = requests.post(url=url_notification,data=new_notification2)

#Testando o código de status HTTP 201
assert result2.status_code == 201
print(result2.status_code)