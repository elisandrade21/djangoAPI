from django.db import models
from enum import Enum
import json
from django_enum_choices.fields import EnumChoiceField


class comunication_type(Enum):
    EMAIL = 'Email'
    SMS = 'Sms'
    PUSH = 'Push'
    WHATSAPP = 'Whatsapp'

class send_status(Enum):
    SENT = 'Sent'
    ERROR = 'Error'
    WAITING = 'Waiting'

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    send_data = models.DateTimeField()
    comunication_type = EnumChoiceField(comunication_type)
    send_status = EnumChoiceField(send_status)
    title = models.CharField(max_length=100)
    body = models.TextField()
    receiver = models.CharField(max_length=150) # receiver will be phone number or email
    name_receiver = models.CharField(max_length=100)

    objects = models.Manager()


    class Meta:
        verbose_name_plural = 'Notifications'


    def __str__(self):
        return self.title

   