from .SeatStatus import SeatStatus, SeatType

class Seat:
    def __init__(self, RowNumber, ColumnNumber, SeatType=SeatType.STANDARD):
        self.RowNumber = RowNumber
        self.ColumnNumber = ColumnNumber
        self.SeatType = SeatType
        self.status = SeatStatus.AVAIBLE

    def StatusChange(self, new_status):
        self.status = new_status

    def TypeChange(self, new_type):
        self.SeatType = new_type