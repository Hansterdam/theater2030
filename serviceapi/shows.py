from datetime import datetime, time, timedelta, date

from . import persistence
from . import films
from . import halls

class Show:

    test_time = datetime.combine(date.today(), time(hour=20, minute=30))

    def __init__(self, values):
        self.id = values['id']
        self.film_id = values['film_id']
        self.hall_id = values['hall_id']
        self.hour = values['hour']
        self.minute = values['minute']

    def is_current(self):
        current_time = datetime.now()
        # current_time = self.test_time

        if self.get_datetime() > current_time:
            return False

        if self.get_end_time() < current_time:
            return False

        return True

    def is_upcomming(self):
        current_time = datetime.now()
        # current_time = self.test_time

        if self.get_datetime() > current_time:
            return True

        return False


    def get_datetime(self):
        return datetime.combine(date.today(), self.get_time())

    def get_time(self):
        return time(hour=self.hour, minute=self.minute)

    def get_pretty_time(self):
        return self.get_time().isoformat(timespec='minutes')

    def get_end_time(self):
        film = self.get_film()
        return self.get_datetime() + timedelta(minutes=film.length)

    def get_film(self):
        if not hasattr(self, 'film'):
            self.film = films.get(self.film_id)

        return self.film

    def get_hall(self):
        if not hasattr(self, 'hall'):
            self.hall = halls.get(self.hall_id)

        return self.hall

    def to_dict(self):
        return {
            'id': self.id,
            'film_id': self.film_id,
            'hall_id': self.hall_id,
            'hour': self.hour,
            'minute': self.minute
        }

    def get_full_dict(self):
        d = self.to_dict()
        d['film'] = self.get_film().to_dict()
        d['hall'] = self.get_hall().to_dict()

        return d

def get(show_id):
    shows = persistence.shows

    for show in shows:
        if show['id'] == show_id:
            return Show(show)

    return None

def get_all():
    shows = persistence.shows

    return list(map(lambda show: Show(show), shows))

def get_upcomming():
    shows = get_all()

    return list(filter(lambda show: show.is_upcomming(), shows))

def get_current():
    shows = get_all()

    current_shows = filter(lambda show: show.is_current(), shows)

    return list(map(lambda show: show.get_full_dict(), current_shows))


def get_next_two():
    upcomming = get_upcomming()

    sorted_shows = sorted(
        upcomming,
        key=lambda show: str(show.hour)+str(show.minute)
    )

    return list(map(lambda show: show.get_full_dict(), sorted_shows[0:2]))

def get_upcomming_for_film(film_id):
    upcomming = get_upcomming()

    film_upcomming = filter(lambda show: show.film_id == film_id, upcomming)

    return list(map(lambda show: show.get_full_dict(), film_upcomming))
