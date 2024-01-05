from django.urls import path
from . import views

urlpatterns = [
    path('chat', views.chat, name='chat'),
    path('<str:room>/', views.room, name='room'),
    path('check_view', views.check_view, name='check_view'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]