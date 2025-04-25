from django.contrib import admin 
from django.urls import path
from availability import views

urlpatterns = [
    path('', views.scheduler, name='scheduler'),
    path('data', views.scheduler_data, name='scheduler-data'),
]
