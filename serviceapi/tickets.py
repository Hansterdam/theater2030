from datetime import timedelta

from . import persistence
from . import shows
from . import seats

class Ticket:

    def __init__(self, values):
        self.id = values['id']
        self.show_id = values['show_id']
        self.seat_id = values['seat_id']
        self.checked_in = values['checked_in']

    def get_show(self):
        if not hasattr(self, 'show'):
            self.show = shows.get(self.show_id)

        return self.show

    def get_seat(self):
        if not hasattr(self, 'seat'):
            self.seat = seats.get(self.seat_id)

        return self.seat

    def check_in(self):
        if self.checked_in:
            raise ValueError('checked_in')

        show_time = self.get_show().get_datetime()
        check_in_time = show_time - timedelta(minutes=10)
        current_time = datetime.now()

        if show_time < current_time or check_in_time > current_time:
            raise Exception('incorrect_time')

        self.store_check_in()

    def store_check_in(self):
        for key, value in persistence.tickets.items:
            if value['id'] == self.id:
                persistence.tickets[key]['checked_in'] = True

    def save(self):
        persistence.tickets.append(self.to_dict())

    def to_dict(self):
        return {
            'id': self.id,
            'show_id': self.show_id,
            'seat_id': self.seat_id,
            'checked_in': self.checked_in
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

def buy(show_id, seat_id):
    ensure_seat_availability(show_id, seat_id)

    id = persistence.get_next_id('tickets')
    ticket = Ticket({'id': id, 'show_id': show_id, 'seat_id': seat_id, 'checked_in': False})

    ticket.save

    return ticket

def ensure_seat_availability(show_id, seat_id):
    bought_tickets = get_for_show(show_id)

    seat_available = True
    for ticket in bought_tickets:
        if ticket.seat_id == seat_id:
            seat_available = False
            break

    if not seat_available:
        raise Exception
