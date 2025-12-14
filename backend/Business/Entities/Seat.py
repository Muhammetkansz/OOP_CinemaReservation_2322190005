from SeatStatus import SeatStatus
from SeatStatus import SeatType
class Seat:
    def __init__(self,Rowletter,Columnnumber,SeatType):
        self.RowNumber = Rowletter
        self.columnletter = Columnnumber
        self.ID = f"{self.Rowletter}{self.Columnnumber}"
        self.SeatType = SeatType
        self.status = SeatStatus.AVAIBLE

    def StatusChange(self):
    pass

    def TypeChange(self):
    pass