class Showtime:
    def __init__(self, id, time, movie, theater):
        self.id = id
        self.time = time
        self.movie = movie      # Showtime aggregates Movie
        self.theater = theater