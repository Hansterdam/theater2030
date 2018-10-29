from django.http import JsonResponse

from . import films
from . import seats
from . import shows
from . import tickets

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

def detail(request, resource, item_id):
    if resource == 'films':
        item = films.get(item_id)
    elif resource == 'shows':
        item = shows.get(item_id)
    else:
        item = {}

    return JsonResponse(to_dict(item), safe=False)

def film_shows(request, film_id):
    film_upcomming = shows.get_upcomming_for_film(film_id)

    return JsonResponse(to_dict(film_upcomming), safe=False)

def show_seats(request, show_id):
    if request.method == 'GET':
        free_seats = seats.get_available_for_show(show_id)

        return JsonResponse(to_dict(free_seats), safe=False)
    elif request.method == 'POST':
        seat_id = int(request.POST['seat_id'])
        try:
            ticket = tickets.buy(show_id, seat_id)
            return JsonResponse(to_dict(ticket), safe=False)
        except Exception:
            err = {'status': 'error', 'message': 'seat not found or occupied'}
            return JsonResponse(err)

def check_in(request, ticket_id):
    ticket = tickets.get(ticket_id)

    try:
        ticket.check_in()
        status = {'status': 'success'}
    except Exception:
        status = {'status': 'error', 'message': 'incorrect time to check in'}
    except ValueError:
        status = {'status': 'error', 'message': 'ticket already checked in'}

    return JsonResponse(status)
