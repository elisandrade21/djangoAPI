from rest_framework import serializers
from rest_enumfield import EnumField
from .models import Notification, comunication_type,send_status 

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('__all__')

    
    send_status = EnumField(choices=send_status, to_choice=lambda x: (x.value, x.name), to_repr=lambda x: x.value)
    comunication_type = EnumField(choices=comunication_type, to_choice=lambda x: (x.value, x.name), to_repr=lambda x: x.value)
