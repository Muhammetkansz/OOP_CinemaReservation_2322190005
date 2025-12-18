from backend.Business.Entities.Theater import Theater
from backend.Business.Entities.Movie import Movie
from backend.Business.Entities.SeatStatus import SeatStatus, SeatType

def main():
    cinema = Theater(1, "Star Cinema", True, 5, 5)
    cinema.initialize_seats()
    
    cinema.display_seats_map()
    
    print(cinema.reserve_seat("A1"))
    print(cinema.reserve_seat("A2"))
    
    fiyat = cinema.calculate_price("A1", "WEEKEND")
    print(f"Bilet Fiyatı: {fiyat} TL")
    
    cinema.display_seats_map()
    print(cinema.cancel_reservation("A2"))
    cinema.display_seats_map()

    movies = [
        Movie(1, "Inception", "Sci-Fi"),
        Movie(2, "The Dark Knight", "Action"),
        Movie(3, "Interstellar", "Sci-Fi"),
        Movie(4, "The Godfather", "Drama")
    ]

    print("\n--- Aksiyon Filmleri (Filtreleme) ---")
    action_movies = [m for m in movies if m.genre == "Action"]
    for m in action_movies:
        print(f"Film: {m.title}")

    print("\n--- Filmler (İsme Göre Sıralı) ---")
    movies.sort(key=lambda x: x.title)
    for m in movies:
        print(f"ID: {m.id} | Film: {m.title} | Tür: {m.genre}")

if __name__ == "__main__":
    main()