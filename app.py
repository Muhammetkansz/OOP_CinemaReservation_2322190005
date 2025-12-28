from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    db_path = os.path.join(os.path.dirname(__file__), 'backend', 'Database', 'movies.json')
    movies = []
    if os.path.exists(db_path):
        with open(db_path, 'r', encoding='utf-8') as f:
            movies = json.load(f)
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)