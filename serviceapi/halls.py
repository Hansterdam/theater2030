from . import persistence

def get_all():
    return persistence.halls

def get(hall_id):
    halls = persistence.halls
    for hall in halls:
        if (hall['id'] == hall_id):
            return hall

    return {'id': 0, 'name': 'No name'}
