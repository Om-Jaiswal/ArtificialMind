from django.urls import path
from . import views

urlpatterns = [
    path('mutetranslator/', views.mutetranslator, name="mutetranslator")
]