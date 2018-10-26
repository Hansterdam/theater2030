from django.http import HttpResponse

from . import persistence

def index(request):
    return HttpResponse(persistence.films)
