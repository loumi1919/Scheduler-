from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import datetime
from .models import Event


def scheduler(request):
    return render(request, 'scheduler.html')


@csrf_exempt
def scheduler_data(request):     
    out = [
        {
            'title': event.description,
            'id': event.id,
            'date': event.date,
            'start': datetime.datetime.combine(event.date, event.start),
            'end': datetime.datetime.combine(event.date, event.end),
            'status':event.status
        } for event in Event.objects.all()
    ]
  
    return JsonResponse(out, safe=False)