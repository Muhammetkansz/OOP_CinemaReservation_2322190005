
class ShowtimeManager:
    def __init__(self):
        self.showtimes = [] 
        
    def add_showtime(self, showtime):
        self.showtimes.append(showtime)

    def filter_showtimes_by_movie(self, movie_name):
        filtered_list = [
            s for s in self.showtimes 
            if s.movie.name.lower() == movie_name.lower()
        ]
        return filtered_list

    def filter_showtimes_by_genre(self, genre_name):
        filtered_list = [
            s for s in self.showtimes 
            if s.movie.genre.lower() == genre_name.lower()
        ]
        return filtered_list

    def filter_showtimes_by_date(self, date_string):
        filtered_list = [
            s for s in self.showtimes 
            if s.date == date_string
        ]
        return filtered_list