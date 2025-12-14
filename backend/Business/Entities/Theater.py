from .Seat import Seat
class Theater:
    def __init__(self, id, name, is_available,total_rows,total_columns):
        self.id = id
        self.name = name
        self.is_available = is_available
        self.totalrows = total_rows
        self.totalcolumns = total_columns
        self.seats = {} # Theater contains seats

    def initialize_seats(self):
        letter = bytearray(b"a")
        
        for i in range(self.totalrows):
            rowletter = letter.decode("latin1")
            for y in range(self.totalcolumns):
                new_seat = Seat(
                    RowNumber = rowletter,
                    columnletter = y + 1,
                SeatType = SeatType.STANDARD
            )
        letter[0] += 1

        def display_seats_map(self):
        print("\n--- Koltuk ID Haritası ---")
        header = "    " 
        for col in range(1, self.totalcolumns + 1):
            header += f"{col:3}" 
        print(header)
        print("-" * len(header))
        letter = bytearray(b"a")
        
        for i in range(self.totalrows):
            rowletter = letter.decode("latin1")
            row_output = f"{rowletter.upper():2} |" 
            
            for y in range(1, self.totalcolumns + 1): 
                seat_id = f"{rowletter.upper()}{y}" 
                row_output += f"{seat_id:3}" 

            print(row_output) 
            letter[0] += 1 
        print("---------------------------")
        



