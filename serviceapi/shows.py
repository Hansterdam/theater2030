from datetime import datetime, time, timedelta, date

from . import persistence
from . import films
from . import halls

def get_current():
    shows = persistence.shows

    current_shows = []
    for show in shows:
        film = films.get(show['film_id'])

        if is_current(show, film):
            current_shows.append(
                {
                    'film': film['title'],
                    'hall': halls.get(show['hall_id'])['name']
                }
            )

    return current_shows

def is_current(show, film):
    current_time = datetime.now()
    current_time = datetime.combine(date.today(), time(hour=20, minute=30))

    show_time = time(hour=show['hour'], minute=show['minute'])
    show_datetime = datetime.combine(date.today(), show_time)

    if show_datetime > current_time:
        return False

    end_time = show_datetime + timedelta(minutes=film['length'])

    if end_time < current_time:
        return False

    return True

def get_next():
    shows = persistence.shows

    next_shows = []
    for show in shows:
        if is_next(show):
            next_shows.append(show)

    sorted_shows = sorted(
        next_shows,
        key=lambda show: str(show['hour'])+str(show['minute'])
    )

    next_two = sorted_shows[0:2]

    next = []
    for show in next_two:
        next.append(
            {
                'film': films.get(show['film_id'])['title'],
                'hall': halls.get(show['hall_id'])['name'],
                'time': time(hour=show['hour'], minute=show['minute']).isoformat(timespec='minutes')
            }
        )

    return next

def is_next(show):
    current_time = datetime.now()
    current_time = datetime.combine(date.today(), time(hour=14, minute=30))

    show_time = time(hour=show['hour'], minute=show['minute'])
    show_datetime = datetime.combine(date.today(), show_time)

    if show_datetime > current_time:
        return True

    return False
