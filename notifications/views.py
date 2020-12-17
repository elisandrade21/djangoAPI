from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from .models import Notification as NoticationModel, send_status
from .serializers import NotificationSerializer

class NotificationAPIView(APIView):
    def get_object(self, pk):
        try:
            return NoticationModel.objects.get(id=pk)
        except NoticationModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print('entre')
        notification = self.get_object(pk)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)

    def get_notifications_by_status(request, status):
        status_r = send_status.SENT
        if status == "error":
            status_r = send_status.ERROR
        elif status == "waiting":
            status_r = send_status.WAITING
        notications = NoticationModel.objects.filter(send_status=status_r)

        data = serializers.serialize("json", notications)

        return HttpResponse(data, content_type='application/json; utf-8')

    def post(self,request):
        serializer = NotificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Message: sucess"},status=status.HTTP_201_CREATED)

    def put(self, request, pk, format=None):
        notifications = NoticationModel.objects.get(id=pk)
        serializer = NotificationSerializer(notifications, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            notifications = NoticationModel.objects.get(id=pk)
            notifications.delete()
            return Response({"Message: sucess"},status=status.HTTP_204_NO_CONTENT)
        except NoticationModel.DoesNotExist:
            raise Http404


