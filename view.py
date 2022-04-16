import functools, pickle
import tkinter as tk
from PIL import Image, ImageTk
import userhanding, user, battle

class Window:

    def __init__(self) -> None:
        """Ablaktulajdonságok alapértelmezett meghatározása.
        """
        self.win = tk.Tk()
        self.win.geometry("1000x750")
        self.win.resizable(False, False)
        self.tryed = False
        self.tryed2 = False
        self.bg_color = "#fac196"

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
        self.loggined_frame_menu.destroy()
        self._Menu_GUI()
    
    def _Attack(self) -> None:
        """Frame kezelés.
        """
        self.loggined_frame_menu.destroy()
        self.Attack_Frame()

    def _back_loggined_from_attack(self) -> None:
        """Frame kezelés, és állapotmentés.
        """
        self.attack_frame.destroy()
        userhanding._save_user(self.u)
        self._Loggined()

    def _Reg(self) -> None:
        """Frame kezelés a regisztráció függvényében.
        """
        succes = userhanding._register(self.username_reg.get(), self.password1_reg.get(), self.password2_reg.get())
        if succes:
            self.register_menu_frame.destroy()
            self.tryed = False
            self._Login_Menu()
        else:
            self.register_menu_frame.destroy()
            self.tryed = True
            self._Register_Menu()

    def _Login(self) -> None:
        """Frame kezelés a bejelentkezés függvényében.
        """
        username = self.username_login.get()
        password = self.password_login.get()
        succes_login = userhanding._login(username=username, password=password)
        if succes_login:
            self.login_frame_menu.destroy()
            self.tryed2 = False
            file = open(f'./users/{username}.obj', "rb")
            self.u = pickle.load(file)
            file.close()
            self._Loggined()
        else:
            self.login_frame_menu.destroy()
            self.tryed2 = True
            self._Login_Menu()

    def _Next_Round(self) -> None:
        """Frame frissités és új kör.
        """
        self.loggined_frame_menu.destroy()
        self.u._next_round()
        userhanding._save_user(self.u)
        self._Loggined()
        
    def _Unit_Event(self, type:str) -> None:
        """Egység vásárlás és állapotmentés.

        Args:
            type (str): Egység típus.
        """
        self.loggined_frame_menu.destroy()
        self.u._make_unit(type)
        userhanding._save_user(self.u)
        self._Loggined()

    def _Building_Event(self, type:str) -> None:
        """Épület fejlesztés és állapotmentés.

        Args:
            type (str): Épület típus
        """
        self.loggined_frame_menu.destroy()
        self.u._upgrade_building(type)
        userhanding._save_user(self.u)
        self._Loggined()
    
    def _Menu_GUI(self) -> None:
        """Menu GUI felülete.
        """
        self.menu_frame = tk.Frame(self.win)
        self.menu_frame.pack()
        self.tryed = False
        self.tryed2 = False
        background_image = ImageTk.PhotoImage(Image.open("imgs/menu_bg.jpg").resize((1000, 750), Image.ANTIALIAS))
        background = tk.Canvas(self.menu_frame, width=1000, height=750)
        background.pack()
        background.background = background_image
        background.create_image(0, 0, anchor=tk.NW, image=background_image)
        login = tk.Button(self.menu_frame, text="Bejelentkezés", bg="black", fg="white", width=50, height=2, command=self._open_login)
        background.create_window(350,200, anchor=tk.NW, window=login)
        register = tk.Button(self.menu_frame, text="Regisztráció", bg="black", fg="white",width=50, height=2, command=self._open_register)
        background.create_window(350,250, anchor=tk.NW, window=register)
        register = tk.Button(self.menu_frame, text="Kilépés", bg="black", fg="white",width=50, height=2, command=self._exit)
        background.create_window(350,300, anchor=tk.NW, window=register)
        maker = tk.Label(self.menu_frame, text="Késszítette: Leyrer Balázs")
        background.create_window(20,700, anchor=tk.NW, window=maker)

    def _Register_Menu(self) -> None:
        """Regisztráció GUI felülete.
        """
        self.register_menu_frame = tk.Frame(self.win)
        self.register_menu_frame.pack()
        background_image = ImageTk.PhotoImage(Image.open("imgs/menu_bg.jpg").resize((1000, 750), Image.ANTIALIAS))
        background = tk.Canvas(self.register_menu_frame, width=1000, height=750)
        background.pack()
        background.background = background_image
        background.create_image(0, 0, anchor=tk.NW, image=background_image)
        reg_frame = tk.Frame(self.register_menu_frame, height=400, width=750, bg=self.bg_color)
        background.create_window(125,150, anchor=tk.NW, window=reg_frame)
        tk.Label(reg_frame, text="Felhasználónév:", bg=self.bg_color).place(x=250, y=50)
        self.username_reg = tk.Entry(reg_frame, width=50)
        self.username_reg.place(x=250, y=70)
        tk.Label(reg_frame, text="Jelszó:", bg=self.bg_color).place(x=250, y=90)
        self.password1_reg = tk.Entry(reg_frame, width=50, show="*")
        self.password1_reg.place(x=250, y=110)
        tk.Label(reg_frame, text="Jelszó ismét:", bg=self.bg_color).place(x=250, y=130)
        self.password2_reg = tk.Entry(reg_frame, width=50, show="*")
        self.password2_reg.place(x=250, y=150)
        tk.Button(reg_frame, text="Regisztráció", command=self._Reg).place(x=250, y=200)
        if self.tryed:
            tk.Label(reg_frame, text="Vagy van már ilyen nevű felhasználó, vagy nem azonos a jelszó!", bg=self.bg_color, fg="#ff0000").place(x=225, y=300)
        tk.Button(reg_frame, text="Vissza", command=self._back_menu_from_reg).place(x=50, y=350)

    def _Login_Menu(self) -> None:
        """Bejelentekzés GUI felülete.
        """
        self.login_frame_menu = tk.Frame(self.win)
        self.login_frame_menu.pack()
        background_image = ImageTk.PhotoImage(Image.open("imgs/menu_bg.jpg").resize((1000, 750), Image.ANTIALIAS))
        background = tk.Canvas(self.login_frame_menu, width=1000, height=750)
        background.pack()
        background.background = background_image
        background.create_image(0, 0, anchor=tk.NW, image=background_image)
        login_frame = tk.Frame(self.login_frame_menu, height=400, width=750, bg=self.bg_color)
        background.create_window(125,150, anchor=tk.NW, window=login_frame)
        tk.Label(login_frame, text="Felhasználónév:", bg=self.bg_color).place(x=250, y=50)
        self.username_login = tk.Entry(login_frame, width=50)
        self.username_login.place(x=250, y=70)
        tk.Label(login_frame, text="Jelszó:", bg=self.bg_color).place(x=250, y=90)
        self.password_login = tk.Entry(login_frame, width=50, show="*")
        self.password_login.place(x=250, y=110)
        tk.Button(login_frame, text="Bejelentkezés", command=self._Login).place(x=250, y=150)
        if self.tryed2:
            tk.Label(login_frame, text="Hibás felhasználónév vagy jelszó!", bg=self.bg_color, fg="#ff0000").place(x=300, y=200)
        tk.Button(login_frame, text="Vissza", command=self._back_menu_from_login).place(x=50, y=350)

    def _Loggined(self):
        """Ez a bejelentekezett felhasználók GUI felülete.
        """
        self.loggined_frame_menu = tk.Frame(self.win)
        self.loggined_frame_menu.pack()
        background_image = ImageTk.PhotoImage(Image.open("imgs/menu_bg.jpg").resize((1000, 750), Image.ANTIALIAS))
        background = tk.Canvas(self.loggined_frame_menu, width=1000, height=750)
        background.pack()
        background.background = background_image
        background.create_image(0, 0, anchor=tk.NW, image=background_image)
        loggined_frame = tk.Frame(self.loggined_frame_menu, height=400, width=750, bg=self.bg_color)
        background.create_window(125,150, anchor=tk.NW, window=loggined_frame)
        tk.Label(loggined_frame, text=f'Felhasználó: {self.u.name}', bg=self.bg_color).place(x=50, y=50)
        gold_image = ImageTk.PhotoImage(Image.open("imgs/gold.jpg").resize((40, 40), Image.ANTIALIAS))
        gold_image_canvas = tk.Canvas(loggined_frame, width=30, height=30, bg=self.bg_color)
        gold_image_canvas.place(x=50, y=85)
        gold_image_canvas.background = gold_image
        gold_image_canvas.create_image(0, 0, anchor=tk.NW, image=gold_image)
        tk.Label(loggined_frame, text=f'{self.u.gold}', bg=self.bg_color).place(x=100, y=90)
        food_imgae = ImageTk.PhotoImage(Image.open("imgs/food.jpg").resize((40, 40), Image.ANTIALIAS))
        food_imgae_canvas = tk.Canvas(loggined_frame, width=30, height=30, bg=self.bg_color)
        food_imgae_canvas.place(x=150, y=85)
        food_imgae_canvas.background = food_imgae
        food_imgae_canvas.create_image(0, 0, anchor=tk.NW, image=food_imgae)
        tk.Label(loggined_frame, text=f'{self.u.food}', bg=self.bg_color).place(x=200, y=90)
        buildings_y_image = 150
        buildings_y_label = 160
        buildings_y_label2 = 210
        buildings_y_button = 180
        units_y_image = 250
        units_y_label = 260
        units_y_label_2 = 310
        units_y_button = 280
        units_height_button = 1
        units_width_button = 3
        farm_image = ImageTk.PhotoImage(Image.open("imgs/farm.jpg").resize((40, 40), Image.ANTIALIAS))
        farm_image_canvas = tk.Canvas(loggined_frame, width=30, height=30, bg=self.bg_color)
        farm_image_canvas.place(x=50, y=buildings_y_image)
        farm_image_canvas.background = farm_image
        farm_image_canvas.create_image(0, 0, anchor=tk.NW, image=farm_image)
        tk.Label(loggined_frame, text=f'{self.u.farm.level}', bg=self.bg_color).place(x=100, y=buildings_y_label)
        tk.Button(loggined_frame, text="+", height=units_height_button, width=units_width_button, command=functools.partial(self._Building_Event, "farm")).place(x=50, y=buildings_y_button)
        tk.Label(loggined_frame, text=f'food: {self.u.farm.foodprice}\ngold: {self.u.farm.goldprice}', bg=self.bg_color).place(x=50, y=buildings_y_label2)
        mine_image = ImageTk.PhotoImage(Image.open("imgs/mine.jpg").resize((40, 40), Image.ANTIALIAS))
        mine_image_canvas = tk.Canvas(loggined_frame, width=30, height=30, bg=self.bg_color)
        mine_image_canvas.place(x=150, y=buildings_y_image)
        mine_image_canvas.background = mine_image
        mine_image_canvas.create_image(0, 0, anchor=tk.NW, image=mine_image)
        tk.Label(loggined_frame, text=f'{self.u.goldmine.level}', bg=self.bg_color).place(x=200, y=buildings_y_label)
        tk.Button(loggined_frame, text="+", height=units_height_button, width=units_width_button, command=functools.partial(self._Building_Event, "goldmine")).place(x=150, y=buildings_y_button)
        tk.Label(loggined_frame, text=f'food: {self.u.goldmine.foodprice}\ngold: {self.u.goldmine.goldprice}', bg=self.bg_color).place(x=150, y=buildings_y_label2)
        spearman_image = ImageTk.PhotoImage(Image.open("imgs/spearman.jpg").resize((40, 40), Image.ANTIALIAS))
        spearman_image_canvas = tk.Canvas(loggined_frame, width=30, height=30, bg=self.bg_color)
        spearman_image_canvas.place(x=50, y=units_y_image)
        spearman_image_canvas.background = spearman_image
        spearman_image_canvas.create_image(0, 0, anchor=tk.NW, image=spearman_image)
        tk.Label(loggined_frame, text=f'{self.u.spear_man.amount}', bg=self.bg_color).place(x=100, y=units_y_label)
        tk.Button(loggined_frame, text="+", height=units_height_button, width=units_width_button, command=functools.partial(self._Unit_Event, "spear")).place(x=50, y=units_y_button)
        tk.Label(loggined_frame, text=f'food: {self.u.spear_man.food_price}\ngold: {self.u.spear_man.gold_price}', bg=self.bg_color).place(x=50, y=units_y_label_2)
        swordman_image = ImageTk.PhotoImage(Image.open("imgs/swordman.jpg").resize((40, 40), Image.ANTIALIAS))
        swordman_image_canvas = tk.Canvas(loggined_frame, width=30, height=30, bg=self.bg_color)
        swordman_image_canvas.place(x=150, y=units_y_image)
        swordman_image_canvas.background = swordman_image
        swordman_image_canvas.create_image(0, 0, anchor=tk.NW, image=swordman_image)
        tk.Label(loggined_frame, text=f'{self.u.sword_man.amount}', bg=self.bg_color).place(x=200, y=units_y_label)
        tk.Button(loggined_frame, text="+", height=units_height_button, width=units_width_button, command=functools.partial(self._Unit_Event, "sword")).place(x=150, y=units_y_button)
        tk.Label(loggined_frame, text=f'food: {self.u.sword_man.food_price}\ngold: {self.u.sword_man.gold_price}', bg=self.bg_color).place(x=150, y=units_y_label_2)
        muskater_image = ImageTk.PhotoImage(Image.open("imgs/muskater.jpg").resize((40, 40), Image.ANTIALIAS))
        muskater_image_canvas = tk.Canvas(loggined_frame, width=30, height=30, bg=self.bg_color)
        muskater_image_canvas.place(x=250, y=units_y_image)
        muskater_image_canvas.background = muskater_image
        muskater_image_canvas.create_image(0, 0, anchor=tk.NW, image=muskater_image)
        tk.Label(loggined_frame, text=f'{self.u.muskater.amount}', bg=self.bg_color).place(x=300, y=units_y_label)
        tk.Button(loggined_frame, text="+", height=units_height_button, width=units_width_button, command=functools.partial(self._Unit_Event, "musket")).place(x=250, y=units_y_button)
        tk.Label(loggined_frame, text=f'food: {self.u.muskater.food_price}\ngold: {self.u.muskater.gold_price}', bg=self.bg_color).place(x=250, y=units_y_label_2)
        light_horse_image = ImageTk.PhotoImage(Image.open("imgs/lighthorse.jpg").resize((40, 40), Image.ANTIALIAS))
        light_horse_image_canvas = tk.Canvas(loggined_frame, width=30, height=30, bg=self.bg_color)
        light_horse_image_canvas.place(x=350, y=units_y_image)
        light_horse_image_canvas.background = light_horse_image
        light_horse_image_canvas.create_image(0, 0, anchor=tk.NW, image=light_horse_image)
        tk.Label(loggined_frame, text=f'{self.u.light_horse.amount}', bg=self.bg_color).place(x=400, y=units_y_label)
        tk.Button(loggined_frame, text="+", height=units_height_button, width=units_width_button, command=functools.partial(self._Unit_Event, "light")).place(x=350, y=units_y_button)
        tk.Label(loggined_frame, text=f'food: {self.u.light_horse.food_price}\ngold: {self.u.light_horse.gold_price}', bg=self.bg_color).place(x=350, y=units_y_label_2)
        armored_horse_image = ImageTk.PhotoImage(Image.open("imgs/armoredhorse.jpg").resize((40, 40), Image.ANTIALIAS))
        armored_horse_image_canvas = tk.Canvas(loggined_frame, width=30, height=30, bg=self.bg_color)
        armored_horse_image_canvas.place(x=450, y=units_y_image)
        armored_horse_image_canvas.background = armored_horse_image
        armored_horse_image_canvas.create_image(0, 0, anchor=tk.NW, image=armored_horse_image)
        tk.Label(loggined_frame, text=f'{self.u.armored_horse.amount}', bg=self.bg_color).place(x=500, y=units_y_label)
        tk.Button(loggined_frame, text="+", height=units_height_button, width=units_width_button, command=functools.partial(self._Unit_Event, "armored")).place(x=450, y=units_y_button)
        tk.Label(loggined_frame, text=f'food: {self.u.armored_horse.food_price}\ngold: {self.u.armored_horse.gold_price}', bg=self.bg_color).place(x=450, y=units_y_label_2)
        tk.Button(loggined_frame, text="Logout", width=10, height=1, command=self._back_menu_from_loggined).place(x = 500, y = 50)
        tk.Button(loggined_frame, text="Next Round", width=10, height=1, command=self._Next_Round).place(x = 600, y = 50)
        tk.Button(loggined_frame, text="Attack", width=10, height=1, command=self._Attack).place(x = 600, y = 100)

    def Attack_Frame(self):
        """Ez a csata felülete és enemy generálás, illetve csata kimenet meghatározás.
        """
        enemy = user.User_save("Enemy", "")
        enemy._make_enemy_stats(self.u.score)
        self.attack_frame = tk.Frame(self.win)
        self.attack_frame.pack()
        background_image = ImageTk.PhotoImage(Image.open("imgs/menu_bg.jpg").resize((1000, 750), Image.ANTIALIAS))
        background = tk.Canvas(self.attack_frame, width=1000, height=750)
        background.pack()
        background.background = background_image
        background.create_image(0, 0, anchor=tk.NW, image=background_image)
        attack_frame = tk.Frame(self.attack_frame, height=400, width=750, bg=self.bg_color)
        background.create_window(125,150, anchor=tk.NW, window=attack_frame)
        tk.Label(attack_frame, text=f'Felhasználó: {self.u.name}', bg=self.bg_color).place(x=50, y=50)
        units_y_image = 100
        units_y_label = 110
        u_spearman_image = ImageTk.PhotoImage(Image.open("imgs/spearman.jpg").resize((40, 40), Image.ANTIALIAS))
        u_spearman_image_canvas = tk.Canvas(attack_frame, width=30, height=30, bg=self.bg_color)
        u_spearman_image_canvas.place(x=50, y=units_y_image)
        u_spearman_image_canvas.background = u_spearman_image
        u_spearman_image_canvas.create_image(0, 0, anchor=tk.NW, image=u_spearman_image)
        tk.Label(attack_frame, text=f'{self.u.spear_man.amount}', bg=self.bg_color).place(x=100, y=units_y_label)
        u_swordman_image = ImageTk.PhotoImage(Image.open("imgs/swordman.jpg").resize((40, 40), Image.ANTIALIAS))
        u_swordman_image_canvas = tk.Canvas(attack_frame, width=30, height=30, bg=self.bg_color)
        u_swordman_image_canvas.place(x=150, y=units_y_image)
        u_swordman_image_canvas.background = u_swordman_image
        u_swordman_image_canvas.create_image(0, 0, anchor=tk.NW, image=u_swordman_image)
        tk.Label(attack_frame, text=f'{self.u.sword_man.amount}', bg=self.bg_color).place(x=200, y=units_y_label)
        u_muskater_image = ImageTk.PhotoImage(Image.open("imgs/muskater.jpg").resize((40, 40), Image.ANTIALIAS))
        u_muskater_image_canvas = tk.Canvas(attack_frame, width=30, height=30, bg=self.bg_color)
        u_muskater_image_canvas.place(x=250, y=units_y_image)
        u_muskater_image_canvas.background = u_muskater_image
        u_muskater_image_canvas.create_image(0, 0, anchor=tk.NW, image=u_muskater_image)
        tk.Label(attack_frame, text=f'{self.u.muskater.amount}', bg=self.bg_color).place(x=300, y=units_y_label)
        u_light_horse_image = ImageTk.PhotoImage(Image.open("imgs/lighthorse.jpg").resize((40, 40), Image.ANTIALIAS))
        u_light_horse_image_canvas = tk.Canvas(attack_frame, width=30, height=30, bg=self.bg_color)
        u_light_horse_image_canvas.place(x=350, y=units_y_image)
        u_light_horse_image_canvas.background = u_light_horse_image
        u_light_horse_image_canvas.create_image(0, 0, anchor=tk.NW, image=u_light_horse_image)
        tk.Label(attack_frame, text=f'{self.u.light_horse.amount}', bg=self.bg_color).place(x=400, y=units_y_label)
        u_armored_horse_image = ImageTk.PhotoImage(Image.open("imgs/armoredhorse.jpg").resize((40, 40), Image.ANTIALIAS))
        u_armored_horse_image_canvas = tk.Canvas(attack_frame, width=30, height=30, bg=self.bg_color)
        u_armored_horse_image_canvas.place(x=450, y=units_y_image)
        u_armored_horse_image_canvas.background = u_armored_horse_image
        u_armored_horse_image_canvas.create_image(0, 0, anchor=tk.NW, image=u_armored_horse_image)
        tk.Label(attack_frame, text=f'{self.u.armored_horse.amount}', bg=self.bg_color).place(x=500, y=units_y_label)
        tk.Label(attack_frame, text=f'{enemy.name}', bg=self.bg_color).place(x=50, y=200)
        e_units_y_image = 200
        e_units_y_label = 210
        e_spearman_image = ImageTk.PhotoImage(Image.open("imgs/spearman.jpg").resize((40, 40), Image.ANTIALIAS))
        e_spearman_image_canvas = tk.Canvas(attack_frame, width=30, height=30, bg=self.bg_color)
        e_spearman_image_canvas.place(x=50, y=e_units_y_image)
        e_spearman_image_canvas.background = e_spearman_image
        e_spearman_image_canvas.create_image(0, 0, anchor=tk.NW, image=e_spearman_image)
        tk.Label(attack_frame, text=f'{enemy.spear_man.amount}', bg=self.bg_color).place(x=100, y=e_units_y_label)
        e_spearman_image = ImageTk.PhotoImage(Image.open("imgs/swordman.jpg").resize((40, 40), Image.ANTIALIAS))
        e_swordman_image_canvas = tk.Canvas(attack_frame, width=30, height=30, bg=self.bg_color)
        e_swordman_image_canvas.place(x=150, y=e_units_y_image)
        e_swordman_image_canvas.background = e_spearman_image
        e_swordman_image_canvas.create_image(0, 0, anchor=tk.NW, image=e_spearman_image)
        tk.Label(attack_frame, text=f'{enemy.sword_man.amount}', bg=self.bg_color).place(x=200, y=e_units_y_label)
        e_spearman_image = ImageTk.PhotoImage(Image.open("imgs/muskater.jpg").resize((40, 40), Image.ANTIALIAS))
        e_muskater_image_canvas = tk.Canvas(attack_frame, width=30, height=30, bg=self.bg_color)
        e_muskater_image_canvas.place(x=250, y=e_units_y_image)
        e_muskater_image_canvas.background = e_spearman_image
        e_muskater_image_canvas.create_image(0, 0, anchor=tk.NW, image=e_spearman_image)
        tk.Label(attack_frame, text=f'{enemy.muskater.amount}', bg=self.bg_color).place(x=300, y=e_units_y_label)
        e_light_horse_image = ImageTk.PhotoImage(Image.open("imgs/lighthorse.jpg").resize((40, 40), Image.ANTIALIAS))
        e_light_horse_image_canvas = tk.Canvas(attack_frame, width=30, height=30, bg=self.bg_color)
        e_light_horse_image_canvas.place(x=350, y=e_units_y_image)
        e_light_horse_image_canvas.background = e_light_horse_image
        e_light_horse_image_canvas.create_image(0, 0, anchor=tk.NW, image=e_light_horse_image)
        tk.Label(attack_frame, text=f'{enemy.light_horse.amount}', bg=self.bg_color).place(x=400, y=e_units_y_label)
        e_armored_horse_image = ImageTk.PhotoImage(Image.open("imgs/armoredhorse.jpg").resize((40, 40), Image.ANTIALIAS))
        e_armored_horse_image_canvas = tk.Canvas(attack_frame, width=30, height=30, bg=self.bg_color)
        e_armored_horse_image_canvas.place(x=450, y=e_units_y_image)
        e_armored_horse_image_canvas.background = e_armored_horse_image
        e_armored_horse_image_canvas.create_image(0, 0, anchor=tk.NW, image=e_armored_horse_image)
        tk.Label(attack_frame, text=f'{enemy.armored_horse.amount}', bg=self.bg_color).place(x=500, y=e_units_y_label)
        if battle._Battle(self.u, enemy):
            tk.Label(attack_frame, text="Győzelem!", bg=self.bg_color).place(x=250, y=280)
            self.u._win()
        else:
            tk.Label(attack_frame, text="Vereség!", bg=self.bg_color).place(x=250, y=280)
            self.u._lose()
            enemy._lose()
        tk.Button(attack_frame, text="OK", width=10, height=1, command=self._back_loggined_from_attack).place(x = 250, y = 350)