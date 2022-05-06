class Moneda():
    
    def __init__(self, name, avrgArea, areaTolerance):
        self.upperAreaLimit = avrgArea + areaTolerance
        self.lowerAreaLimit = avrgArea - areaTolerance
        self.quantity = 0
        self.name = name
        