from django.urls import path
from . import views

urlpatterns = [
    path('walktalkie/', views.walktalkie, name="walktalkie")
]