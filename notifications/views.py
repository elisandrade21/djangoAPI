from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404


from .models import Notification as NoticationModel
from .serializers import NotificationSerializer

class NotificationAPIView(APIView):
    def get_object(self,pk):
        try:
            return NoticationModel.objects.get(id=pk)
        except NoticationModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        notifications = NoticationModel.objects.all()
        serializer = NotificationSerializer(notifications, many = True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

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
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NoticationModel.DoesNotExist:
            raise Http404


