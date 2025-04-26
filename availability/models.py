from django.db import models
from django.contrib.auth import get_user_model

from django.db.models import Q
from django.core.exceptions import ValidationError

User = get_user_model()


class Event(models.Model):
    """
    Event model
    """ 
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank = True)
    end = models.DateTimeField(null=True, blank = True)

    class Meta:
        db_table = 'Mes évènements'
    def clean(self):
        start_in_range = Q(start__lte=self.start, end__gte=self.start)
        end_in_range = Q(start__lte=self.end, end__gte=self.end)
        # Queryset that finds all clashing timeslots with the same day
        queryset = self._meta.default_manager.filter(start_in_range | end_in_range)
        if self.pk:
            queryset = queryset.exclude(pk=self.pk) # Exclude this object if it is already saved to the database
        if queryset.exists():
            raise ValidationError("Vous avez déjà un évènement sur ce créneau!")
        
    def __str__(self) -> str:
        return str(self.description)