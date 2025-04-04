from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [  
    path('gestion/', views.gestion_medica_view, name='gestion_medica_view'),
]