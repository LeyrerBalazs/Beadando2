class spear_man:

    def __init__(self) -> None:
        """Lándzsás egység tulajdonságai.
        """
        self.amount = 0
        self.hp = 50
        self.defense = 10
        self.attack = 5
        self.gold_price = 20
        self.food_price = 50

class sword_man:

    def __init__(self) -> None:
        """Kardos egység tulajdonságai.
        """
        self.amount = 0
        self.hp = 50
        self.defense = 5
        self.attack = 15
        self.gold_price = 10
        self.food_price = 60

class muskater:

    def __init__(self) -> None:
        """Muskétás egység tulajdonásgai.
        """
        self.amount = 0
        self.hp = 40
        self.defense = 2
        self.attack = 50
        self.gold_price = 60
        self.food_price = 50

class light_horse:

    def __init__(self) -> None:
        """Könnyű lovas egység tulajdonságai.
        """
        self.amount = 0
        self.hp = 70
        self.defense = 10
        self.attack = 20
        self.gold_price = 50
        self.food_price = 100
    
class armored_horse:
    
    def __init__(self) -> None:
        """Nehéz lovas egység tulajdonságai.
        """
        self.amount = 0
        self.hp = 200
        self.defense = 30
        self.attack = 20
        self.gold_price = 100
        self.food_price = 140