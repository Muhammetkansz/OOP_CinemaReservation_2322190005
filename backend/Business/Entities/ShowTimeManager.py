class ShowtimeManager:
    def __init__(self):
        self.showtimes = [] 
        
    def add_showtime(self, showtime):
        self.showtimes.append(showtime)

    def filter_showtimes_by_movie(self, movie_name):
        return [s for s in self.showtimes if s.movie.name.lower() == movie_name.lower()]

    def filter_showtimes_by_genre(self, genre_name):
        return [s for s in self.showtimes if s.movie.genre.lower() == genre_name.lower()]

    def filter_showtimes_by_date(self, date_string):
        return [s for s in self.showtimes if s.date == date_string]