import passcrypt, units, buildings, random

class User_save:

    def __init__(self, name:str, password:str) -> None:
        """Felhasználó alapbeállításai.

        Args:
            name (str): Felhasználónév.
            password (str): Jelszó.
        """
        self.name = name
        self.password = passcrypt.caesar(password)
        self.gold = 100
        self.food = 100
        self.farm = buildings.Farm()
        self.goldmine = buildings.Goldmine()
        self.spear_man = units.spear_man()
        self.sword_man = units.sword_man()
        self.muskater = units.muskater()
        self.light_horse = units.light_horse()
        self.armored_horse = units.armored_horse()
        self.score = 0
        self.resources = 6000

    def _upgrade_building(self, type:str) -> None:
        """Adott felhasználó épületének fejlesztése.

        Args:
            type (str): Épület típusa.
        """
        if type == "farm":
            if self.farm.goldprice <= self.gold and self.farm.foodprice <= self.food:
                self.gold -= self.farm.goldprice
                self.food -= self.farm.foodprice
                self.farm.goldprice += 600
                self.farm.foodprice += 600
                self.farm.production += 300
                self.farm.level += 1
        elif type == "goldmine":
            if self.goldmine.goldprice <= self.gold and self.goldmine.foodprice <= self.food:
                self.gold -= self.goldmine.goldprice
                self.food -= self.goldmine.foodprice
                self.goldmine.goldprice += 2000
                self.goldmine.foodprice += 2000
                self.goldmine.production += 200
                self.goldmine.level += 1

    def _make_unit(self, type:str):
        """Egység hozzáadása.

        Args:
            type (str): Egység típusa
        """
        if type == "spear":
            if self.spear_man.gold_price <= self.gold and self.spear_man.food_price <= self.food:
                self.gold -= self.spear_man.gold_price
                self.food -= self.spear_man.food_price
                self.spear_man.amount += 1
                self.score += 2
        elif type == "sword":
            if self.sword_man.gold_price <= self.gold and self.sword_man.food_price <= self.food:
                self.gold -= self.sword_man.gold_price
                self.food -= self.sword_man.food_price
                self.sword_man.amount += 1
                self.score += 2
        elif type == "musket":
            if self.muskater.gold_price <= self.gold and self.muskater.food_price <= self.food:
                self.gold -= self.muskater.gold_price
                self.food -= self.muskater.food_price
                self.muskater.amount += 1
                self.score += 4
        elif type == "light":
            if self.light_horse.gold_price <= self.gold and self.light_horse.food_price <= self.food:
                self.gold -= self.light_horse.gold_price
                self.food -= self.light_horse.food_price
                self.light_horse.amount += 1
                self.score += 5
        elif type == "armored":
            if self.armored_horse.gold_price <= self.gold and self.armored_horse.food_price <= self.food:
                self.gold -= self.armored_horse.gold_price
                self.food -= self.armored_horse.food_price
                self.armored_horse.amount += 1
                self.score += 10

    def _next_round(self):
        """Következő kör.
        """
        self.gold += self.goldmine.production
        self.food += self.farm.production

    def _win(self):
        """Ha nyer a csatában.
        """
        self.gold += random.randrange(50, 500)
        self.food += random.randrange(50, 1000)

    def _lose(self):
        """Ha veszít a csatában.
        """
        self.spear_man.amount = 0
        self.sword_man.amount = 0
        self.muskater.amount = 0
        self.light_horse.amount = 0
        self.armored_horse.amount = 0
        self.gold -= random.randrange(50, 500)
        self.food -= random.randrange(50, 1000)

    def _make_enemy_stats(self, score:float):
        """Enemy egység generálása a játékoshoz mérten.

        Args:
            score (float): Játékos egységpontjai
        """
        score2 = score 
        while self.score < score - 15:
            what = random.randint(0, 5)
            if what == 0:
                allowed_unit = int(round(score / 2) / 2)
                self.spear_man.amount += random.randrange(0, allowed_unit)
            elif what == 1:
                allowed_unit = int(round(score / 2)  / 2)
                self.sword_man.amount += random.randrange(0, allowed_unit)
            elif what == 2:
                allowed_unit = int(round(score / 4) / 2)
                self.muskater.amount += random.randrange(0, allowed_unit)
            elif what == 3:
                allowed_unit = int(round(score / 5) / 2)
                self.light_horse.amount += random.randrange(0, allowed_unit)
            elif what == 4:
                allowed_unit = int(round(score / 10) / 2)
                self.armored_horse.amount += random.randrange(0, allowed_unit)
            self.score = self.spear_man.amount * 2 + self.sword_man.amount * 2 + self.muskater.amount * 4 + self.light_horse.amount * 5 + self.armored_horse.amount * 10
            score2 -= self.score