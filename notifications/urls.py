from django.urls import path
from . views import NotificationAPIView
from . views import get_notifications_by_status

urlpatterns = [
    path('notifications/', NotificationAPIView.as_view(),name='notifications'),
    path('notifications/<int:pk>/',NotificationAPIView.as_view(), name='notification'),
    path('notifications/<str:status>/', get_notifications_by_status, name='notifications-filter'),

]


