from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.first,name='first'),
     path('patient',views.patient,name='patient'),
]