from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


from notifications.models import Notification
from .serializers import NotificationSerializer

class NotificationAPIView(APIView):
    def get(self, request):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many = True)
        return Response(serializer.data)

