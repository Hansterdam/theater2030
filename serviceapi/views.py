from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder

from datetime import time, datetime

import json

from . import films
from . import shows

class MyClassEncoder(DjangoJSONEncoder):

    def default(self, obj):
        if isinstance(obj, films.Film):
            return json.dumps(obj.to_dict())

        return super().default(obj)

def home(request):
    welcome = {
        'message': 'Welcome at the service api',
        'current_shows': shows.get_current(),
        'next_shows': shows.get_next_two()
    }
    return JsonResponse(welcome)

def index(request, resource):
    if resource == 'films':
        all = films.get_all()
    elif resource == 'shows':
        all = shows.get_upcomming()
    else:
        all = []

    return JsonResponse(to_dict(all), safe=False)

def detail(request, resource, film_id):
    if resource == 'films':
        item = films.get(film_id)
    else:
        item = {}

    return JsonResponse(to_dict(item), safe=False)

def film_shows(request, film_id):
    film_upcomming = shows.get_upcomming_for_film(film_id)

    return JsonResponse(to_dict(film_upcomming), safe=False)

def to_dict(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            obj[key] = to_dict(value)

        return obj
    elif isinstance(obj, list):
        return list(map(lambda item: to_dict(item), obj))
    else:
        try:
            return obj.to_dict()
        except:
            return obj
