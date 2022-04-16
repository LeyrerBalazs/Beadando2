import userhanding

def _is_same_password(password1:str, password2:str) -> bool:
    """Megállapítja, hogy azonosak e a jelszavak.

    Args:
        password1 (str): Jelszó.
        password2 (str): Másik jelszó.

    Returns:
        bool: True = azonos, False = nem azonos.
    """
    return password1 == password2

def _isnt_same_user(username:str) -> bool:
    """Létezik-e már a felhasználó.

    Args:
        username (str): Felhasználónév

    Returns:
        bool: True = nincs, False = van.
    """
    users = userhanding._load_users()
    allow = True
    for us in users:
        if us == username:
            allow = False
    return allow

def _is_same_user(username:str, user:str) -> bool:
    """Azonos-e a felhasználónév.

    Args:
        username (str): Felhasználónév.
        user (str): Másik felhasználónév.

    Returns:
        bool: True = azonos, False = nem azonos.
    """
    return username == user