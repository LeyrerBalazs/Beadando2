import passcrypt, units, buildings, random, exception

class ActiveUser:

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
        self.maxres = 6500

    def upgrade_building(self, type:str) -> None:
        """Adott felhasználó épületének fejlesztése.

        Args:
            type (str): Épület típusa.
        """
        if type == "farm":
            if self.farm.goldprice <= self.gold and self.farm.foodprice <= self.food and self.farm.level < self.farm.maxlevel:
                self.gold -= self.farm.goldprice
                self.food -= self.farm.foodprice
                self.farm.upgrade()
        elif type == "goldmine":
            if self.goldmine.goldprice <= self.gold and self.goldmine.foodprice <= self.food and self.goldmine.level < self.goldmine.maxlevel:
                self.gold -= self.goldmine.goldprice
                self.food -= self.goldmine.foodprice
                self.goldmine.upgrade()

    def make_unit(self, type:str):
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

    def next_round(self):
        """Következő kör.
        """
        if exception.overthanmax(self.maxres, self.gold + self.goldmine.production):
            self.gold = 6000
        else:
            self.gold += self.goldmine.production
        if exception.overthanmax(self.maxres, self.food + self.farm.production):
            self.food = 6000
        else:
            self.food += self.farm.production

    def win(self):
        """Ha nyer a csatában.
        """
        self.gold += random.randrange(50, 500)
        self.food += random.randrange(50, 1000)

    def lose(self):
        """Ha veszít a csatában.
        """
        self.spear_man.amount = 0
        self.sword_man.amount = 0
        self.muskater.amount = 0
        self.light_horse.amount = 0
        self.armored_horse.amount = 0
        self.gold -= random.randrange(50, 500)
        self.food -= random.randrange(50, 1000)

    def make_enemy_stats(self, score:float):
        """Enemy egység generálása a játékoshoz mérten.

        Args:
            score (float): Játékos egységpontjai
        """
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