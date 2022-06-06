import userhanding

def is_same_password(password1:str, password2:str) -> bool:
    """Megállapítja, hogy azonosak e a jelszavak.

    Args:
        password1 (str): Jelszó.
        password2 (str): Másik jelszó.

    Returns:
        bool: True = azonos, False = nem azonos.
    """
    return password1 == password2

def is_username_unused(username:str) -> bool:
    """Létezik-e már a felhasználó.

    Args:
        username (str): Felhasználónév

    Returns:
        bool: True = nincs, False = van.
    """
    return not username in userhanding.load_users()

def is_same_user(username:str, user:str) -> bool:
    """Azonos-e a felhasználónév.

    Args:
        username (str): Felhasználónév.
        user (str): Másik felhasználónév.

    Returns:
        bool: True = azonos, False = nem azonos.
    """
    return username == user

def overthanmax(max:int, value:int) -> None:
    return max < value

def is_null(summary_attack:int) -> int:
    """Nullával való osztás hibájának kiszűrése

    Args:
        summary_attack (int): Vizsgálanadó szám

    Returns:
        int: Visszaadott érték
    """
    if summary_attack == 0: 
        return 1
    else:
        return summary_attack