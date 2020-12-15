from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id','send_data','comunication_type', 'send_status','title','body']     
        extra_kwargs = {
            'name_receiver' : {'write_only': True},
            'receiver' : {'write_only': True}
        }
