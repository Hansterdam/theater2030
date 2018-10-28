from . import persistence

class Film:

    def __init__(self, values):
        self.id = values['id']
        self.title = values['title']
        self.length = values['length']

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'length': self.length
        }


def get_all(dict=False):
    films = persistence.films

    return list(map(lambda film: Film(film), films))

def get(film_id, dict=False):
    films = persistence.films

    for film in films:
        if (film['id'] == film_id):
            return Film(film)

    return None
