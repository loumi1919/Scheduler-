from django.contrib import admin 
from django.urls import path
from api import views

urlpatterns = [
    path('events', views.EventListCreateView.as_view(), name='events'),
    path('events/<int:id>', views.EventDetailView.as_view(), name='event-detail'),
]
