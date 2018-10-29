def get_next_id(resource):
    if resource == 'tickets':
        last_item = tickets[-1]

    return last_item['id'] + 1

halls = [
    {'id': 1, 'name': 'Grote zaal'},
    {'id': 2, 'name': 'Kleine zaal'},
]

seats = [
    {'id': 1, 'hall_id': 1, 'row': 'A', 'number': 1},
    {'id': 2, 'hall_id': 1, 'row': 'A', 'number': 2},
    {'id': 3, 'hall_id': 1, 'row': 'A', 'number': 3},
    {'id': 4, 'hall_id': 1, 'row': 'A', 'number': 4},
    {'id': 5, 'hall_id': 1, 'row': 'B', 'number': 1},
    {'id': 6, 'hall_id': 1, 'row': 'B', 'number': 2},
    {'id': 7, 'hall_id': 1, 'row': 'B', 'number': 3},
    {'id': 8, 'hall_id': 1, 'row': 'B', 'number': 4},
    {'id': 9, 'hall_id': 1, 'row': 'C', 'number': 1},
    {'id': 10, 'hall_id': 1, 'row': 'C', 'number': 2},
    {'id': 11, 'hall_id': 1, 'row': 'C', 'number': 3},
    {'id': 12, 'hall_id': 1, 'row': 'C', 'number': 4},
    {'id': 13, 'hall_id': 2, 'row': 'A', 'number': 1},
    {'id': 14, 'hall_id': 2, 'row': 'A', 'number': 2},
    {'id': 15, 'hall_id': 2, 'row': 'A', 'number': 3},
    {'id': 16, 'hall_id': 2, 'row': 'B', 'number': 1},
    {'id': 17, 'hall_id': 2, 'row': 'B', 'number': 2},
    {'id': 18, 'hall_id': 2, 'row': 'B', 'number': 3},
]

films = [
    {'id': 1, 'title': 'Her', 'length': 126},
    {'id': 2, 'title': 'Leaning Into the Wind', 'length': 97},
]

shows = [
    {'id': 1, 'film_id': 1, 'hall_id': 1, 'hour': 14, 'minute': 0},
    {'id': 2, 'film_id': 2, 'hall_id': 2, 'hour': 14, 'minute': 30},
    {'id': 3, 'film_id': 2, 'hall_id': 1, 'hour': 16, 'minute': 30},
    {'id': 4, 'film_id': 1, 'hall_id': 2, 'hour': 16, 'minute': 45},
    {'id': 5, 'film_id': 1, 'hall_id': 1, 'hour': 18, 'minute': 30},
    {'id': 6, 'film_id': 2, 'hall_id': 2, 'hour': 19, 'minute': 15},
    {'id': 7, 'film_id': 2, 'hall_id': 1, 'hour': 21, 'minute': 0},
    {'id': 8, 'film_id': 1, 'hall_id': 2, 'hour': 21, 'minute': 15},
]

tickets = [
    {'id': 1, 'show_id': 1, 'seat_id': 1, 'checked_in': False},
    {'id': 2, 'show_id': 2, 'seat_id': 13, 'checked_in': False},
    {'id': 3, 'show_id': 3, 'seat_id': 2, 'checked_in': False},
    {'id': 4, 'show_id': 4, 'seat_id': 14, 'checked_in': True},
    {'id': 5, 'show_id': 5, 'seat_id': 3, 'checked_in': False},
    {'id': 6, 'show_id': 6, 'seat_id': 15, 'checked_in': False},
    {'id': 7, 'show_id': 7, 'seat_id': 4, 'checked_in': False},
    {'id': 8, 'show_id': 8, 'seat_id': 16, 'checked_in': True},
    {'id': 9, 'show_id': 1, 'seat_id': 5, 'checked_in': False},
    {'id': 10, 'show_id': 2, 'seat_id': 17, 'checked_in': False},
    {'id': 11, 'show_id': 3, 'seat_id': 6, 'checked_in': False},
    {'id': 12, 'show_id': 4, 'seat_id': 18, 'checked_in': True},
    {'id': 13, 'show_id': 5, 'seat_id': 7, 'checked_in': False},
    {'id': 14, 'show_id': 6, 'seat_id': 13, 'checked_in': False},
    {'id': 15, 'show_id': 7, 'seat_id': 8, 'checked_in': False},
    {'id': 16, 'show_id': 8, 'seat_id': 14, 'checked_in': True},
    {'id': 17, 'show_id': 1, 'seat_id': 9, 'checked_in': False},
    {'id': 18, 'show_id': 2, 'seat_id': 15, 'checked_in': False},
    {'id': 19, 'show_id': 3, 'seat_id': 10, 'checked_in': False},
    {'id': 20, 'show_id': 4, 'seat_id': 16, 'checked_in': True},
    {'id': 21, 'show_id': 5, 'seat_id': 11, 'checked_in': False},
    {'id': 22, 'show_id': 6, 'seat_id': 17, 'checked_in': False},
    {'id': 23, 'show_id': 7, 'seat_id': 12, 'checked_in': False},
    {'id': 24, 'show_id': 8, 'seat_id': 18, 'checked_in': True},
    {'id': 25, 'show_id': 1, 'seat_id': 2, 'checked_in': False},
    {'id': 26, 'show_id': 2, 'seat_id': 14, 'checked_in': False},
    {'id': 27, 'show_id': 3, 'seat_id': 3, 'checked_in': False},
    {'id': 28, 'show_id': 4, 'seat_id': 15, 'checked_in': True},
    {'id': 29, 'show_id': 5, 'seat_id': 4, 'checked_in': False},
    {'id': 30, 'show_id': 6, 'seat_id': 16, 'checked_in': False},
]
