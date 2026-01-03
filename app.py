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
    theater_id = request.args.get('theater_id', 1, type=int)
    theater_name = f"Salon {theater_id}"
    
    my_theater = Theater(id=theater_id, name=theater_name, is_available=True, total_rows=8, total_columns=10)
    my_theater.initialize_seats()
    
    movies = load_json('movies.json')
    current_movie = next((m for m in movies if m['id'] == movie_id), None)
    recommendations = [m for m in movies if m['genre'] == current_movie['genre'] and m['id'] != movie_id]
    
    seat_list = []
    for seat_id, seat_obj in my_theater.seats.items():
        is_vip = seat_id.startswith('A') or seat_id.startswith('B')
        seat_list.append({
            'number': seat_id,
            'isOccupied': seat_obj.status == SeatStatus.RESERVED,
            'isVIP': is_vip
        })
    
    seat_list.sort(key=lambda x: x['number'])
    return render_template('seats.html', seats=seat_list, movie_id=movie_id, recommendations=recommendations, theater_name=theater_name)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    selected_seats = data.get('seats', [])
    my_theater = Theater(id=1, name="Salon 1", is_available=True, total_rows=8, total_columns=10)
    my_theater.initialize_seats()
    total_price = 0
    for seat_id in selected_seats:
        if seat_id.startswith('A') or seat_id.startswith('B'):
            my_theater.seats[seat_id].SeatType = my_theater.seats[seat_id].SeatType.VIP
        price = my_theater.calculate_price(seat_id, "WEEKDAY")
        total_price += price
    return jsonify({'total_price': total_price})

@app.route('/suggest_best', methods=['POST'])
def suggest_best():
    best_seats = ["D5", "D6", "E5", "E6"]
    return jsonify({'suggested': best_seats})

@app.route('/admin/analytics')
def analytics():
    movies = load_json('movies.json')
    revenue_data = [{"title": m['title'], "revenue": 500} for m in movies]
    return render_template('admin.html', revenue_data=revenue_data)

if __name__ == '__main__':
    app.run(debug=True)