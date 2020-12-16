from django.urls import path
from . views import NotificationAPIView


urlpatterns = [
   
    path('notifications/', NotificationAPIView.as_view(),name='notifications'),
    path('notifications/<int:pk>/', NotificationAPIView.as_view(),name='delete')

]
