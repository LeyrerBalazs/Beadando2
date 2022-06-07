class unit:
    def __init__(self, hp:int, defense:int, attack:int, gold_price:int, food_price:int, score:int, name:str, image:str) -> None:
        """Unitoktípusú objektumok beállítása kezdetben

        Args:
            hp (int): Életerő
            defense (int): Védekezés
            attack (int): Támadás
            gold_price (int): Arany ár
            food_price (int): Kaja ár
            name (str): Név
            score (int): Pontszám
        """
        self.amount = 0
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.gold_price = gold_price
        self.food_price = food_price
        self.score = score
        self.image = image

class spear_man (unit):

    def __init__(self) -> None:
        """Lándzsás egység tulajdonságai.
        """
        super().__init__(hp = 50, defense = 10, attack = 5, gold_price = 20, food_price = 50, score = 3, name = "spear", image = "imgs/spearman.jpg")

class sword_man (unit):

    def __init__(self) -> None:
        """Kardos egység tulajdonságai.
        """
        super().__init__(hp = 50, defense = 5, attack = 15, gold_price = 10, food_price = 60, score = 1, name = "sword", image = "imgs/swordman.jpg")

class muskater (unit):

    def __init__(self) -> None:
        """Muskétás egység tulajdonásgai.
        """
        super().__init__(hp = 40, defense = 2, attack = 50, gold_price = 60, food_price = 50, score = 4, name = "musket", image = "imgs/muskater.jpg")

class light_horse (unit):

    def __init__(self) -> None:
        """Könnyű lovas egység tulajdonságai.
        """
        super().__init__(hp = 70, defense = 10, attack = 20, gold_price = 50, food_price = 100, score = 3, name = "light", image = "imgs/lighthorse.jpg")
    
class armored_horse (unit):

    def __init__(self) -> None:
        """Nehéz lovas egység tulajdonságai.
        """
        super().__init__(hp = 200, defense = 30, attack = 20, gold_price = 100, food_price = 140, score = 5, name = "armored", image="imgs/armoredhorse.jpg")