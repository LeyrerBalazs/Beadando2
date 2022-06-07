import functools, pickle, time, threading
import tkinter as tk
from PIL import Image, ImageTk
import userhanding, battle, user

class Window:

    def __init__(self) -> None:
        """Ablaktulajdonságok alapértelmezett meghatározása.
        """
        self.time = 60
        self.win = tk.Tk()
        self.bg_color = "#fac196"
        self.win.geometry("1000x750")
        self.win.resizable(False, False)
        self.win.title("Leyrer Balázs Beadnadó 22t")
        self.tried = False # volt-e sikertelen regisztrációs probálkozás
        self.tried2 = False # volt-e sikertelen bejelentkezéses probálkozás
        self.s = threading.Thread(target=self._Round)

    def _exit(self) -> None:
        """Kilépés.
        """
        self.win.destroy()

    def _open_register(self) -> None:
        """Frame kezelés.
        """
        self.menu_frame.destroy()
        self._Register_Menu()

    def _open_login(self) -> None:
        """Frame kezelés.
        """
        self.menu_frame.destroy()
        self._Login_Menu()

    def _back_menu_from_reg(self) -> None:
        """Frame kezelés.
        """
        self.register_menu_frame.destroy()
        self._Menu_GUI()

    def _back_menu_from_login(self) -> None:
        """Frame kezelés.
        """
        self.login_frame_menu.destroy()
        self._Menu_GUI()

    def _back_menu_from_loggined(self) -> None:
        """Frame kezelés.
        """
        self.loggined_frame_menu.pack_forget()
        self._Menu_GUI()
    
    def _Attack(self) -> None:
        """Frame kezelés.
        """
        self.loggined_frame_menu.pack_forget()
        self.Attack_Frame()

    def _back_loggined_from_attack(self) -> None:
        """Frame kezelés, és állapotmentés.
        """
        self.attack_frame.destroy()
        userhanding.save_user(self.u)
        self._Loggined()

    def _Reg(self) -> None:
        """Frame kezelés a regisztráció függvényében.
        """
        succes = userhanding.register(self.username_reg.get(), self.password1_reg.get(), self.password2_reg.get())
        if succes:
            self.register_menu_frame.destroy()
            self.tried = False
            self._Login_Menu()
        else:
            self.register_menu_frame.destroy()
            self.tried = True
            self._Register_Menu()

    def _Login(self) -> None:
        """Frame kezelés a bejelentkezés függvényében.
        """
        username = self.username_login.get()
        password = self.password_login.get()
        succes_login = userhanding.login(username=username, password=password)
        if succes_login:
            self.tried2 = False
            self.login_frame_menu.destroy()  
            file = open(f'./users/{username}.obj', "rb")
            self.u = pickle.load(file)
            file.close()
            self._Loggined()
        else:
            self.tried2 = True
            self.login_frame_menu.destroy()
            self._Login_Menu()

    def _Round(self):
        """Mellékszál függvénye, időszámítás, következő kör
        """
        while True:
            time.sleep(1)
            self.time -= 1
            self.timelabel.configure(text=f"Time: {self.time} s")
            if self.time == 0:
                self.time = 60
                self._Next_Round()

    def _Next_Round(self) -> None:
        """Frame frissités és új kör.
        """
        self.u.next_round()
        userhanding.save_user(self.u)
        self.foodlabel.configure(text=f'{self.u.food}')
        self.goldlabel.configure(text=f'{self.u.gold}')
        
    def _Unit_Event(self, type:str, loggined_frame:tk.Frame) -> None:
        """Egység vásárlás és állapotmentés.

        Args:
            type (str): Egység típus.
        """
        self.u.make_unit(type)
        userhanding.save_user(self.u)
        self.goldlabel.configure(text=f"{self.u.gold}")
        self.foodlabel.configure(text=f"{self.u.food}")
        self.WriteUnits_InLoggined(loggined_frame, 250, 260, 310, 280, self.u, 3, 1)  

    def _Building_Event(self, type:str, frame:tk.Frame) -> None:
        """Épület fejlesztés és állapotmentés.

        Args:
            type (str): Épület típus
        """
        self.u.upgrade_building(type)
        self.WriteBuilds(frame)
        userhanding.save_user(self.u)
        self.goldlabel.configure(text=f"{self.u.gold}")
        self.foodlabel.configure(text=f"{self.u.food}")
    
    def Make_BG(self, frame:tk.Frame) -> None:
        """Háttérkép megjelenítése

        Args:
            frame (tkinter.Frame): A frame amelyre pakoljuk.

        Returns:
            tkinter.Frame: Visszaadja a módosított frame-et.
        """
        background_image = ImageTk.PhotoImage(Image.open("imgs/menu_bg.jpg").resize((1000, 750), Image.ANTIALIAS))
        background = tk.Canvas(frame, width=1000, height=750)
        background.pack()
        background.background = background_image
        background.create_image(0, 0, anchor=tk.NW, image=background_image)
        bgframe = tk.Frame(frame, height=400, width=750, bg=self.bg_color)
        background.create_window(125,150, anchor=tk.NW, window=bgframe)
        return bgframe

    def WriteImgs(self, frame:tk.Frame, image_y:int, images:list, xloc:int):
        """Megjelenítti a képeket

        Args:
            frame (tk.Frame): Frame amin megjelenik
            image_y (int): y koordináta
            images (list): Képek elérési útja
            xloc (int): x koordináta kezdeti helye
        """
        for imginimages in images:
            img = ImageTk.PhotoImage(Image.open(imginimages).resize((40, 40), Image.ANTIALIAS))
            img_canvas = tk.Canvas(frame, width=30, height=30, bg=self.bg_color)
            img_canvas.place(x=xloc, y=image_y)
            img_canvas.background = img
            img_canvas.create_image(0, 0, anchor=tk.NW, image=img)
            xloc += 100

    def WriteUnits(self, frame:tk.Frame, image_y:int) -> None:
        """Unit képek kiírása

        Args:
            frame (tkinter.Frame): Frame amire kiírjuk 
            image_y (int): Képek y koordinátája
        """
        images = []
        for unit in self.u.units:
            images.append(unit.image)
        self.WriteImgs(frame, image_y, images, 50)

    def WriteUnits_InAttack(self, frame:tk.Frame, image_y:int, label_y:int, type:str, user:object) -> None:  
        """Attack Frame Unit kiírás

        Args:
            frame (tkinter.Frame): _description_
            image_y (int): Képek y koordinátája
            label_y (int): Mennyiség y koordinátája
            user (ActiveUser object): Az ActiveUser object az adatok kiírásához
        """
        xloc = 100
        units = []
        if type == "user":
            for unit in user.units:
                units.append(unit)
        elif type == "enemy":
            for unit in user.enemyunits:
                units.append(unit)
        print(units)
        for unit in units:
            tk.Label(frame, text=f'{unit.amount}', bg=self.bg_color).place(x=xloc, y=label_y)
            xloc += 100
        self.WriteUnits(frame, image_y)

    def WriteUnits_InLoggined(self, frame, image_y, label_y, label_y2, button_y, user, w, h) -> None:
        """Loggined Unit kiírás

        Args:
            frame (tkinter.Frame): Frame amire kiírjuk
            image_y (int): Képek y koordinátája
            label_y (int): Mennyiség y koordinátája
            label_y2 (int): Ár y koordinátája
            button_y (int): Gomb y koordinátája
            user (ActiveUser object): Az ActiveUser object az adatok kiírásához
            w (int): Gombszélessége
            h (int): Gombmagassága
        """
        xloc_1 = 100
        xloc_2 = 50
        for unit in user.units:
            tk.Label(frame, text=f'{unit.amount}', bg=self.bg_color).place(x=xloc_1, y=label_y)
            tk.Button(frame, text="+", height=h, width=w, command=functools.partial(self._Unit_Event, unit.name, frame)).place(x=xloc_2, y=button_y)
            tk.Label(frame, text=f'food: {unit.food_price}\ngold: {unit.gold_price}', bg=self.bg_color).place(x=xloc_2, y=label_y2)
            xloc_1 += 100
            xloc_2 += 100
        self.WriteUnits(frame, image_y)

    def WriteBuilds(self, frame:tk.Frame):
        """Kiíratja az épületeket

        Args:
            frame (tk.Frame): Amire kiírja
        """
        xloc_1 = 100
        xloc_2 = 50
        images = []
        for build in self.u.builds:
            images.append(build.image)
        self.WriteImgs(frame, 150, images, 50)
        for build in self.u.builds:
            tk.Label(frame, text=f'{build.level}', bg=self.bg_color).place(x=xloc_1, y=160)
            tk.Button(frame, text="+", height=1, width=3, command=functools.partial(self._Building_Event, build.name, frame)).place(x=xloc_2, y=180)
            if build.level == build.maxlevel:
                tk.Label(frame, text="Max", bg=self.bg_color).place(x=xloc_2, y=210)
            else:
                tk.Label(frame, text=f'food: {build.foodprice}\ngold: {build.goldprice}', bg=self.bg_color).place(x=xloc_2, y=210)
            xloc_1 += 100
            xloc_2 += 100  

    def _Menu_GUI(self) -> None:
        """Menu GUI felülete.
        """
        self.time = 60
        self.menu_frame = tk.Frame(self.win)
        self.menu_frame.pack()
        self.tried = False
        self.tried2 = False
        background_image = ImageTk.PhotoImage(Image.open("imgs/menu_bg.jpg").resize((1000, 750), Image.ANTIALIAS))
        background = tk.Canvas(self.menu_frame, width=1000, height=750)
        background.pack()
        background.background = background_image
        background.create_image(0, 0, anchor=tk.NW, image=background_image)
        login = tk.Button(self.menu_frame, text="Login", bg="black", fg="white", width=50, height=2, command=self._open_login)
        background.create_window(350,200, anchor=tk.NW, window=login)
        register = tk.Button(self.menu_frame, text="Register", bg="black", fg="white",width=50, height=2, command=self._open_register)
        background.create_window(350,250, anchor=tk.NW, window=register)
        register = tk.Button(self.menu_frame, text="Exit", bg="black", fg="white",width=50, height=2, command=self._exit)
        background.create_window(350,300, anchor=tk.NW, window=register)
        maker = tk.Label(self.menu_frame, text="Creator: Leyrer Balázs")
        background.create_window(20,700, anchor=tk.NW, window=maker)

    def _Register_Menu(self) -> None:
        """Regisztráció GUI felülete.
        """
        self.register_menu_frame = tk.Frame(self.win)
        self.register_menu_frame.pack()
        reg_frame = self.Make_BG(self.register_menu_frame)
        tk.Label(reg_frame, text="Username:", bg=self.bg_color).place(x=250, y=50)
        self.username_reg = tk.Entry(reg_frame, width=50)
        self.username_reg.place(x=250, y=70)
        tk.Label(reg_frame, text="Password:", bg=self.bg_color).place(x=250, y=90)
        self.password1_reg = tk.Entry(reg_frame, width=50, show="*")
        self.password1_reg.place(x=250, y=110)
        tk.Label(reg_frame, text="Password again:", bg=self.bg_color).place(x=250, y=130)
        self.password2_reg = tk.Entry(reg_frame, width=50, show="*")
        self.password2_reg.place(x=250, y=150)
        tk.Button(reg_frame, text="Register", command=self._Reg).place(x=250, y=200)
        if self.tried:
            tk.Label(reg_frame, text="Either there is already a user with that name, or the password is not the same!", bg=self.bg_color, fg="#ff0000").place(x=225, y=300)
        tk.Button(reg_frame, text="Back", command=self._back_menu_from_reg).place(x=50, y=350)

    def _Login_Menu(self) -> None:
        """Bejelentekzés GUI felülete.
        """
        self.login_frame_menu = tk.Frame(self.win)
        self.login_frame_menu.pack()
        login_frame = self.Make_BG(self.login_frame_menu)
        tk.Label(login_frame, text="Username:", bg=self.bg_color).place(x=250, y=50)
        self.username_login = tk.Entry(login_frame, width=50)
        self.username_login.place(x=250, y=70)
        tk.Label(login_frame, text="Password:", bg=self.bg_color).place(x=250, y=90)
        self.password_login = tk.Entry(login_frame, width=50, show="*")
        self.password_login.place(x=250, y=110)
        tk.Button(login_frame, text="Login", command=self._Login).place(x=250, y=150)
        if self.tried2:
            tk.Label(login_frame, text="Incorrect username or password!", bg=self.bg_color, fg="#ff0000").place(x=300, y=200)
        tk.Button(login_frame, text="Back", command=self._back_menu_from_login).place(x=50, y=350)

    def _Loggined(self):
        """Ez a bejelentekezett felhasználók GUI felülete.
        """
        if not self.s.is_alive():
            self.s.setDaemon(True)
            self.s.start()
        self.loggined_frame_menu = tk.Frame(self.win)
        self.loggined_frame_menu.pack()
        loggined_frame = self.Make_BG(self.loggined_frame_menu)
        self.WriteImgs(loggined_frame, 85, ["imgs/gold.jpg", "imgs/food.jpg"], 50)
        tk.Label(loggined_frame, text=f'User: {self.u.name}', bg=self.bg_color).place(x=50, y=50)
        self.goldlabel = tk.Label(loggined_frame, text=f'{self.u.gold}', bg=self.bg_color)
        self.goldlabel.place(x=100, y=90)
        self.foodlabel = tk.Label(loggined_frame, text=f'{self.u.food}', bg=self.bg_color)
        self.foodlabel.place(x=200, y=90)
        self.WriteBuilds(loggined_frame)
        tk.Button(loggined_frame, text="Logout", width=10, height=1, command=self._back_menu_from_loggined).place(x = 500, y = 50)
        self.timelabel = tk.Label(loggined_frame, text=f"Time: {self.time} s", font=15, bg=self.bg_color)
        self.timelabel.place(x = 600, y = 50)
        tk.Button(loggined_frame, text="Attack", width=10, height=1, command=self._Attack).place(x = 600, y = 100)
        self.WriteUnits_InLoggined(loggined_frame, 250, 260, 310, 280, self.u, 3, 1)

    def Attack_Frame(self):
        """Ez a csata felülete és enemy generálás, illetve csata kimenet meghatározás.
        """
        self.u.make_enemy_stats()
        self.attack_frame = tk.Frame(self.win)
        self.attack_frame.pack()
        attack_frame = self.Make_BG(self.attack_frame)
        tk.Label(attack_frame, text=f'User: {self.u.name}', bg=self.bg_color).place(x=50, y=50)
        self.WriteUnits_InAttack(attack_frame, 100, 110, "user", self.u)
        tk.Label(attack_frame, text=f'Enemy:', bg=self.bg_color).place(x=50, y=180)
        self.WriteUnits_InAttack(attack_frame, 200, 210, "enemy", self.u)
        if battle.Battle(self.u) == 0:
            tk.Label(attack_frame, text="Win!", fg="#1c8a1d", font=25, bg=self.bg_color).place(x=250, y=280)
            self.u.win()
        elif battle.Battle(self.u) == 1:
            tk.Label(attack_frame, text="Lose!", fg="#ff0000", font=25, bg=self.bg_color).place(x=250, y=280)
            self.u.lose()
        elif battle.Battle(self.u) == 2:
            tk.Label(attack_frame, text="Döntetlen!", font=25, bg=self.bg_color).place(x=250, y=280)
        tk.Button(attack_frame, text="OK", width=10, height=1, command=self._back_loggined_from_attack).place(x = 300, y = 350)