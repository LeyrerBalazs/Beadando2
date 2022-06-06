class House:
    
    def __init__(self, maxlevel:int, goldprice:int, plusfoodprice:int, plusgoldprice:int, plusproduction:int, name:str) -> None:
        """Beállítja a öröklödött házobjektumok értékét

        Args:
            maxlevel (int): Maximum elérhető szint
            goldprice (int): Arany ár
            plusfoodprice (int): Kaja árnövekedés
            plusgoldprice (int): Arany ár növekedés
            plusproduction (int): Termelés növekedés
            name (str): Neve
        """
        self.level = 1
        self.production = 10
        self.maxlevel = maxlevel
        self.foodprice = 50
        self.goldprice = goldprice
        self.plusfoodprice = plusfoodprice
        self.plusgoldprice = plusgoldprice
        self.production = plusproduction
        self.name = name

    def upgrade(self):
        """Ez fejleszti az adott épülettípust
        """
        self.goldprice += self.plusfoodprice
        self.foodprice += self.plusgoldprice
        self.production += self.production
        self.level += 1

class Farm (House):
    
    def __init__(self) -> None:
        """Farm épület tulajdonságai.
        """
        super().__init__(maxlevel = 10, goldprice = 10, plusfoodprice = 600, plusgoldprice = 600 , plusproduction = 300, name = "farm")

class Goldmine (House):

    def __init__(self) -> None:
        """Aranybánya épület tulajdonságai.
        """
        super().__init__(maxlevel = 5, goldprice = 50, plusfoodprice = 2000, plusgoldprice = 2000 , plusproduction = 600, name = "goldmine")