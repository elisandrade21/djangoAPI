from django.db import models

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    name_receiver = models.CharField(max_length=150)
    receiver = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    send_data = models.DateTimeField()
    notification_type = models.CharField(max_length=50)
    send_status = models.BooleanField(default=False)
    id_message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return  self.notification_type

