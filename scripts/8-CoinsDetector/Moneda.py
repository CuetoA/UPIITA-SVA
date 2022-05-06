class Moneda():
    
    def __init__(self, name, upperAreaLimit, lowerAreaLimit):
        self.upperAreaLimit = upperAreaLimit
        self.lowerAreaLimit = lowerAreaLimit
        self.quantity = 0
        self.name = name
        