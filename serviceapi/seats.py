from . import persistence

from . import halls
from . import shows
from . import tickets

class Seat:

    def __init__(self, values):
        self.id = values['id']
        self.hall_id = values['hall_id']
        self.row = values['row']
        self.number = values['number']

    def to_dict(self):
        return {
            'id': self.id,
            'hall_id': self.hall_id,
            'row': self.row,
            'number': self.number
        }

    def get_hall(self):
        if not hasattr(self, 'hall'):
            self.hall = halls.get(self.hall_id)

        return self.hall

def get_all():
    seats = persistence.seats

    return list(map(lambda seat: Seat(seat), seats))

def get(seat_id):
    seats = persistence.seats

    for seat in seats:
        if (seat['id'] == seat_id):
            return Seat(seat)

    return None

def get_for_hall(hall_id):
    seats = get_all()

    return list(filter(lambda seat: seat.hall_id == hall_id, seats))

def get_available_for_show(show_id):
    show = shows.get(show_id)
    seats = get_for_hall(show.hall_id)
    tickets_for_show = tickets.get_for_show(show_id)
    taken_seat_ids = list(map(lambda ticket: ticket.seat_id, tickets_for_show))


    return list(filter(lambda seat: seat.id not in taken_seat_ids, seats))
