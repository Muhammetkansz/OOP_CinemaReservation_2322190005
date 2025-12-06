class Theater:
    def __init__(self, id, name, is_available):
        self.id = id
        self.name = name
        self.is_available = is_available
        self.seats = [] # Theater contains seats