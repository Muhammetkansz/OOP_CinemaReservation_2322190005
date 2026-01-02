from flask import Flask, render_template, request, jsonify
import json
import os
from backend.Business.Entities.Theater import Theater
from backend.Business.Entities.SeatStatus import SeatStatus

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
    my_theater = Theater(id=1, name="Salon 1", is_available=True, total_rows=8, total_columns=10)
    my_theater.initialize_seats()
    
    seat_list = []
    for seat_id, seat_obj in my_theater.seats.items():
        seat_list.append({
            'number': seat_id,
            'isOccupied': seat_obj.status == SeatStatus.RESERVED,
            'isVIP': seat_obj.SeatType.name == "VIP"
        })
    
    seat_list.sort(key=lambda x: x['number'])
    return render_template('seats.html', seats=seat_list, movie_id=movie_id)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    selected_seats = data.get('seats', [])
    total_price = len(selected_seats) * 60 
    return jsonify({'total_price': total_price})

if __name__ == '__main__':
    app.run(debug=True)