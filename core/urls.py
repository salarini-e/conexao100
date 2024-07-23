from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('pre-inscricao/', views.preinscricao),
]
