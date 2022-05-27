class unit:
    def __init__(self, hp:int, defense:int, attack:int, gold_price:int, food_price:int) -> None:
        self.amount = 0
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.gold_price = gold_price
        self.food_price = food_price

class spear_man (unit):

    def __init__(self) -> None:
        """Lándzsás egység tulajdonságai.
        """
        super().__init__(hp = 50, defense = 10, attack = 5, gold_price = 20, food_price = 50)

class sword_man (unit):

    def __init__(self) -> None:
        """Kardos egység tulajdonságai.
        """
        super().__init__(hp = 50, defense = 5, attack = 15, gold_price = 10, food_price = 60)

class muskater (unit):

    def __init__(self) -> None:
        """Muskétás egység tulajdonásgai.
        """
        super().__init__(hp = 40, defense = 2, attack = 50, gold_price = 60, food_price = 50)

class light_horse (unit):

    def __init__(self) -> None:
        """Könnyű lovas egység tulajdonságai.
        """
        super().__init__(hp = 70, defense = 10, attack = 20, gold_price = 50, food_price = 100)
    
class armored_horse (unit):

    def __init__(self) -> None:
        """Nehéz lovas egység tulajdonságai.
        """
        super().__init__(hp = 200, defense = 30, attack = 20, gold_price = 100, food_price = 140)