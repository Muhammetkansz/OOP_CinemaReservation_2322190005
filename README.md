# CinemaReservation
🎬 Cinema Reservation & Management System
A comprehensive web-based cinema management system built with Python, Flask, and OOP principles. This project covers all stages of development, from core business logic to an interactive web interface.

🚀 Key Features
🔹 Stage 1 & 2: Core Logic & Management
Object-Oriented Design: Implementation of Theater, Movie, Seat, and SeatStatus classes for a robust backend architecture.

Dynamic Pricing Engine: Automatic price calculation based on seat type (VIP/Standard) and time (Weekday/Weekend).

Ticket Management: Functional seat reservation and real-time cancellation systems.

Data Handling: Advanced sorting and filtering of movies by title and genre.

🔹 Stage 3: Advanced Web Interface
Interactive Seat Map: A dynamic, grid-based UI for real-time seat selection using Flask and Jinja2 templates.

Optimal Seat Suggestion: A smart algorithm that automatically identifies and selects the best available seats closest to the screen center.

Recommendation System: A "Customers also liked" feature that suggests movies based on genre similarity.

Admin Dashboard: Real-time tracking of total revenue, occupancy rates, and sales analytics.

🛠️ Installation & Setup
Clone the Repository:

Bash

git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
Install Dependencies:

Bash

pip install flask
Run the Application:

Bash

python app.py
Access the app at http://127.0.0.1:5000

📁 Project Structure
app.py: The main Flask server and API routes.

main.py: Entry point for console-based testing of core business logic.

backend/: Contains all Python classes and entity models.

templates/: HTML files for the web frontend.

movies.json: JSON-based database for movie information.

.gitignore: Prevents unnecessary files (like __pycache__) from being uploaded.

📝 Technologies Used
Backend: Python 3.x, Flask

Frontend: HTML5, CSS3 (Flexbox/Grid), JavaScript (Fetch API)

Data: JSON
