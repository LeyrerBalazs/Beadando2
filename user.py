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
        self.builds = [buildings.Farm(), buildings.Goldmine()]
        self.units = [units.spear_man(), units.sword_man(), units.muskater(), units.light_horse(), units.armored_horse()]
        self.score = 0
        self.maxres = 10000

    def upgrade_building(self, type:str) -> None:
        """Adott felhasználó épületének fejlesztése.

        Args:
            type (str): Épület típusa.
        """
        for build in self.builds:
            if build.name == type:
                if build.goldprice <= self.gold and build.foodprice <= self.food and build.level < build.maxlevel:
                    self.gold -= build.goldprice
                    self.food -= build.foodprice
                    build.upgrade()

    def make_unit(self, type:str):
        """Egység hozzáadása.

        Args:
            type (str): Egység típusa
        """
        for unit in self.units:
            if unit.name == type and unit.gold_price <= self.gold and unit.food_price <= self.food:
                self.gold -= unit.gold_price
                self.food -= unit.food_price
                unit.amount += 1
                self.score += unit.score        

    def next_round(self):
        """Következő kör.
        """
        if exception.overthanmax(self.maxres, self.gold + self.builds[0].production):
            self.gold = 10000
        else:
            self.gold += self.builds[0].production
        if exception.overthanmax(self.maxres, self.food + self.builds[1].production):
            self.food = 10000
        else:
            self.food += self.builds[1].production

    def win(self):
        """Ha nyer a csatában.
        """
        self.gold += random.randrange(50, 500)
        self.food += random.randrange(50, 1000)
        self.score += 1

    def lose(self):
        """Ha veszít a csatában.
        """
        for unit in self.units:
            unit.amount = 0
        self.gold -= random.randrange(50, 500)
        self.food -= random.randrange(50, 1000)
        self.score = 0

    def make_enemy_stats(self, score:float):
        """Enemy egység generálása a játékoshoz mérten.

        Args:
            score (float): Játékos egységpontjai
        """
        while self.score < score - 10:
            what = random.randint(0, len(self.units)-1)
            allowed_unit = int(round(score / self.units[what].score) / 2)
            self.units[what].amount += random.randrange(0, allowed_unit)
            self.score = 0
            for unit in self.units:
                self.score += unit.amount * unit.score