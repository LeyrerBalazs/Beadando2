from numpy import imag


class House:
    
    def __init__(self, maxlevel:int, goldprice:int, plusfoodprice:int, plusgoldprice:int, plusproduction:int, name:str, image:str) -> None:
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
        self.name = name
        self.image = image
        self.foodprice = 50
        self.production = 10
        self.maxlevel = maxlevel
        self.goldprice = goldprice
        self.production = plusproduction
        self.plusfoodprice = plusfoodprice
        self.plusgoldprice = plusgoldprice

    def upgrade(self):
        """Ez fejleszti az adott épülettípust
        """
        self.level += 1
        self.production += self.production
        self.goldprice += self.plusfoodprice
        self.foodprice += self.plusgoldprice

class Farm (House):
    
    def __init__(self) -> None:
        """Farm épület tulajdonságai.
        """
        super().__init__(maxlevel = 10, goldprice = 10, plusfoodprice = 600, plusgoldprice = 600 , plusproduction = 300, name = "farm", image="imgs/farm.jpg")

class Goldmine (House):

    def __init__(self) -> None:
        """Aranybánya épület tulajdonságai.
        """
        super().__init__(maxlevel = 5, goldprice = 50, plusfoodprice = 2000, plusgoldprice = 2000 , plusproduction = 600, name = "goldmine", image="imgs/mine.jpg")