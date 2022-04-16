class Farm:
    
    def __init__(self) -> None:
        """Farm épület tulajdonságai.
        """
        self.level = 1
        self.production = 10
        self.maxlevel = 10
        self.foodprice = 50
        self.goldprice = 50

class Goldmine:

    def __init__(self) -> None:
        """Aranybánya épület tulajdonságai.
        """
        self.level = 1
        self.production = 10
        self.maxlevel = 5
        self.foodprice = 50
        self.goldprice = 50