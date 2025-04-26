from rest_framework import serializers

from availability.models import Event

class EventSerializer(serializers.ModelSerializer[Event]):
    """
    Event List View.
    Get all events and Create one. 
    """
    name = serializers.StringRelatedField()
    title = serializers.StringRelatedField()
    
    class Meta:
        model = Event
        fields = "__all__"
        examples = [
            {
                "name": "Lumi",
                "title": "Présentation projet",
                "description": "Présentation projet",
                "start" : "2025-04-26T10:30:00Z",
                "end" : "025-04-26T18:30:00Z"
            }
        ]