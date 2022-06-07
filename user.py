import passcrypt, units, buildings, random, exception

class ActiveUser:

    def __init__(self, name:str, password:str) -> None:
        """Felhasználó alapbeállításai.

        Args:
            name (str): Felhasználónév.
            password (str): Jelszó.
        """
        self.score = 0
        self.gold = 100
        self.food = 100
        self.name = name
        self.maxres = 10000
        self.password = passcrypt.caesar(password)
        self.builds = [buildings.Farm(), buildings.Goldmine()]
        self.units = [units.spear_man(), units.sword_man(), units.muskater(), units.light_horse(), units.armored_horse()]
        self.enemyunits = [units.spear_man(), units.sword_man(), units.muskater(), units.light_horse(), units.armored_horse()]

    def upgrade_building(self, type:str) -> None:
        """Adott felhasználó épületének fejlesztése.

        Args:
            type (str): Épület típusa.
        """
        for build in self.builds:
            if build.name == type:
                if build.goldprice <= self.gold and build.foodprice <= self.food and build.level < build.maxlevel:
                    build.upgrade()
                    self.gold -= build.goldprice
                    self.food -= build.foodprice

    def make_unit(self, type:str):
        """Egység hozzáadása.

        Args:
            type (str): Egység típusa
        """
        for unit in self.units:
            if unit.name == type and unit.gold_price <= self.gold and unit.food_price <= self.food:
                unit.amount += 1
                self.score += unit.score  
                self.gold -= unit.gold_price
                self.food -= unit.food_price      

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
        self.score += 1
        for unit in self.enemyunits:
            unit.amount = 0
        self.gold += random.randrange(50, 500)
        self.food += random.randrange(50, 1000)   

    def lose(self):
        """Ha veszít a csatában.
        """
        self.score = 0
        for unit in self.units:
            unit.amount = 0
        for unit in self.enemyunits:
            unit.amount = 0
        self.gold -= random.randrange(50, 500)
        self.food -= random.randrange(50, 1000)

    def make_enemy_stats(self):
        """Enemy egység generálása a játékoshoz mérten.

        Args:
            score (float): Játékos egységpontjai
        """
        enemyscore = 0
        while enemyscore < self.score - 15:
            what = random.randint(0, len(self.enemyunits)-1)
            allowed_unit = int(round(self.score / self.enemyunits[what].score) / 2)
            self.enemyunits[what].amount += random.randrange(0, allowed_unit)
            for unit in self.enemyunits:
                enemyscore += unit.amount * unit.score