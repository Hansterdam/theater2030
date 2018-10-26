from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from datetime import time, datetime

from . import films

def index(request):
    welcome = {
        'message': 'Welcome at the service api',
        'time': datetime.now().time().isoformat(timespec='minutes')
    }
    return JsonResponse(welcome)

def film_index(request):
    all_films = films.get_all()
    return JsonResponse(all_films, safe=False)

def film_detail(request, film_id):
    film = films.get(film_id)
    return JsonResponse(film)
