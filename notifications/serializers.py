from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'nome_receiver' : {'write_only': True},
            'receiver' : {'write_only': True}
        }
        model: Notification
        fields = (
            'id',
            'send_data',
            'comunication_type',
            'send_status',
            'title',
            'body'

        )

