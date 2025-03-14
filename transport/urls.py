from django.urls import path
from . import views

urlpatterns = [
    path('', views.transports, name='transports'),
    path('drive/<int:pk>/', views.transport, name='transport'),
    path('map/', views.map, name='map'),
    path('add_alert/', views.add_alert, name='add_alert'),
    path('requests/', views.requests, name='requests'),
    path('requests/accept-request/<int:pk>/', views.accept_request, name='accept_request'),
]