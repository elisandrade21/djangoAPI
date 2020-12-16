from django.urls import path
from . views import NotificationAPIView


urlpatterns = [
   #path('notifications/<int:pk>', NotificationAPIView.as_view(),name='get_test'),
    path('notifications/<str:status>', NotificationAPIView.as_view(),name='status'),
    path('notifications/', NotificationAPIView.as_view(),name='notifications'),
    path('notifications/<int:pk>/', NotificationAPIView.as_view(),name='delete')

]

