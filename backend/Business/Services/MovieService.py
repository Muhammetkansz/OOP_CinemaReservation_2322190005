import json
import os
from backend.Business.Entities.Movie import Movie

class MovieService:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'Database', 'movies.json')

    def get_all_movies(self):
        try:
            if not os.path.exists(self.db_path):
                return []
            with open(self.db_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Movie(m.get('id'), m.get('title'), m.get('genre')) for m in data]
        except Exception:
            return []