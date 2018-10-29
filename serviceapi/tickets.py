from . import persistence
from . import shows
from . import seats

class Ticket:

    def __init__(self, values):
        self.id = values['id']
        self.show_id = values['show_id']
        self.seat_id = values['seat_id']

    def get_show(self):
        if not hasattr(self, 'show'):
            self.show = shows.get(self.show_id)

        return self.show

    def get_seat(self):
        if not hasattr(self, 'seat'):
            self.seat = seats.get(self.seat_id)

        return self.seat

    def to_dict(self):
        return {
            'id': self.id,
            'show_id': self.show_id,
            'seat_id': self.seat_id
        }

def get_all():
    tickets = persistence.tickets

    return list(map(lambda ticket: Ticket(ticket), tickets))

def get(ticket_id):
    tickets = persistence.tickets

    for ticket in tickets:
        if (ticket['id'] == ticket_id):
            return Ticket(ticket)

    return None

def get_for_show(show_id):
    tickets = get_all()

    return list(filter(lambda ticket: ticket.show_id == show_id, tickets))
