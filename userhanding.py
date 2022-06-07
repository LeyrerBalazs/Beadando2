import exception, user, pickle, os, passcrypt

def register(username:str, password1:str, password2:str) -> bool:
    """Ez a függvény felel a regisztrációért

    Args:
        username (str): Felhasználónév.
        password1 (str): Jelszó.
        password2 (str): Megerősítő jelszó.

    Returns:
        bool: Sikeres a regisztráció vagy nem, True = sikeres, False = sikertelen.
    """
    if exception.is_username_unused(username) and exception.is_same_password(password1, password2):
        u = user.ActiveUser(username, password1)
        save_user(u)
        return True
    else:
        return False

def load_users() -> list:
    """Segédfüggvény, megállapítja milyen felhasználók vannak már.

    Returns:
        list: Felhasználók listája
    """
    users = []
    userfiles = os.listdir("./users")
    for userinfile in userfiles:
        users.append(os.path.splitext(userinfile)[0])
    return users

def login(username:str, password:str) -> bool:
    """Ez a függvény határozza meg, hogy sikeres-e a bejelentkezés az adott
    felhasználóba.

    Args:
        username (str): Felhasználónév.
        password (str): Jelszó.

    Returns:
        bool: Sikeres-e a bejelentezés, True = sikeres, False = sikertelen.
    """
    try:
        with open(f'./users/{username}.obj', "rb") as file:
            u = pickle.load(file)
        return exception.is_same_password(password1=u.password, password2=passcrypt.caesar(password))
    except:
        return False

def save_user(user:object) -> None:
    """Elmenti az adott felhasználó állapotát.

    Args:
        user (object): A felhasználó.
    """
    fajl = open(f'users/{user.name}.obj', "wb")
    pickle.dump(user, fajl)
    fajl.close()