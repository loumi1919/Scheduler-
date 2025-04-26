from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import datetime
from .models import Event


def scheduler(request):
    return render(request, 'scheduler.html')
