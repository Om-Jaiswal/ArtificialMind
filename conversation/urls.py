from django.urls import path
from . import views

urlpatterns = [
    path('conversation/', views.conversation, name="conversation"),
    path('<str:room>/', views.room, name="room"),
    path('conversation/checkview', views.checkview, name="checkview"),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages')
]