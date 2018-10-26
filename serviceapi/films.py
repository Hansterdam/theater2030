from . import persistence

def get_all():
    return persistence.films

def get(film_id):
    films = persistence.films
    for film in films:
        if (film['id'] == film_id):
            return film

    return {'id': 0, 'title': 'No title', 'length': 0}
