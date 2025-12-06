class Reservation:
    def __init__(self, id, seat, showtime, is_cancelled):
        self.id = id
        self.seat = seat          # Reservation linked to Seat
        self.showtime = showtime  # Reservation linked to Showtime
        self.is_cancelled = is_cancelled