from .SeatStatus import SeatStatus, SeatType
from .Seat import Seat

class Theater:
    def __init__(self, id, name, is_available, total_rows, total_columns):
        self.id = id
        self.name = name
        self.is_available = is_available
        self.totalrows = total_rows
        self.totalcolumns = total_columns
        self.seats = {}

    def initialize_seats(self):
        letter = bytearray(b"a")
        for i in range(self.totalrows):
            rowletter = letter.decode("latin1").upper()
            for y in range(self.totalcolumns):
                col_number = y + 1
                seat_id = f"{rowletter}{col_number}"
                new_seat = Seat(
                    RowNumber=rowletter,
                    ColumnNumber=col_number,
                    SeatType=SeatType.STANDARD
                )
                self.seats[seat_id] = new_seat
            letter[0] += 1

    def display_seats_map(self):
        print("\n--- Koltuk Haritası (O: Boş, X: Dolu, V: VIP Boş) ---")
        header = "    " 
        for col in range(1, self.totalcolumns + 1):
            header += f"{col:3}" 
        print(header)
        print("-" * len(header))
        
        letter = bytearray(b"a")
        for i in range(self.totalrows):
            rowletter = letter.decode("latin1").upper()
            row_output = f"{rowletter:2} |" 
            
            for y in range(1, self.totalcolumns + 1): 
                seat_id = f"{rowletter}{y}" 
                seat = self.seats.get(seat_id)
                
                symbol = " ? " 
                if seat:
                    if seat.status == SeatStatus.RESERVED:
                        symbol = " X "
                    elif seat.SeatType == SeatType.VIP:
                        symbol = " V "
                    else:
                        symbol = " O "
                        
                row_output += f"{symbol:3}" 

            print(row_output) 
            letter[0] += 1 
        print("-" * len(header))

    def calculate_price(self, seat_id, showtime_type):
        price = 50
        
        if seat_id not in self.seats:
            return "Hata: Koltuk bulunamadı."
            
        seat = self.seats[seat_id]
        
        if seat.SeatType == SeatType.VIP:
            price += 15
            
        if showtime_type.upper() == "WEEKEND":
            price += 10
            
        return price

    def reserve_seat(self, seat_id):
        if seat_id in self.seats:
            seat = self.seats[seat_id]
            if seat.status == SeatStatus.AVAIBLE:
                seat.status = SeatStatus.RESERVED
                return f"{seat_id} başarıyla rezerve edildi."
            else:
                return f"{seat_id} zaten dolu."
        return "Koltuk bulunamadı."

    def cancel_reservation(self, seat_id):
        if seat_id in self.seats:
            seat = self.seats[seat_id]
            if seat.status == SeatStatus.RESERVED:
                seat.status = SeatStatus.AVAIBLE
                return f"{seat_id} rezervasyonu iptal edildi."
            else:
                return f"{seat_id} zaten boş."
        return "Koltuk bulunamadı."


