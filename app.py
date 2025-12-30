from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

def load_json(filename):
    path = os.path.join(os.path.dirname(__file__), 'backend', 'Database', filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

@app.route('/')
def index():
    movies = load_json('movies.json')
    return render_template('index.html', movies=movies)

@app.route('/seats/<int:movie_id>')
def seats(movie_id):
    all_seats = load_json('seats.json')
    movie_seats = [s for s in all_seats if s.get('movieId') == movie_id]
    return render_template('seats.html', seats=movie_seats)

if __name__ == '__main__':
    app.run(debug=True)