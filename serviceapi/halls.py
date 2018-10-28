from . import persistence

class Hall:

    def __init__(self, values):
        self.id = values['id']
        self.name = values['name']

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

def get_all():
    halls = persistence.halls

    return list(map(lambda hall: Hall(hall), halls))

def get(hall_id):
    halls = persistence.halls

    for hall in halls:
        if (hall['id'] == hall_id):
            return Hall(hall)

    return None
