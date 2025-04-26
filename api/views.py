from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics

from availability.models import Event
from .serializers import EventSerializer
# Create your views here.
from django.contrib.auth import get_user_model


User = get_user_model()

class EventListCreateView(generics.ListCreateAPIView[Event]):
    """
    Event List View.
    Get all Event and Create one. 
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user.username
        out = [
        {
            'title':event.description,
            'name': user,
            'description': event.description,
            'start': event.start,
            'end': event.end,
        } for event in Event.objects.all()
        ]
        return out
        
    
    def perform_create(self, serializer):
        # The request user is set as author automatically.
        serializer.save(name=self.request.user)
        

class EventDetailView(generics.RetrieveUpdateDestroyAPIView[Event]):
    """
    Event Detail View. 
    Get/Edit/Delete an Event.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'id'
    