import exception

def _get_hp(user: object) -> int:
    """Életerő kiszámítása

    Args:
        user (object): Adott felhasználó

    Returns:
        int: Életerő értéke
    """
    return user.spear_man.hp * user.spear_man.amount + user.sword_man.hp * user.sword_man.amount + user.muskater.hp * user.muskater.amount + user.light_horse.hp * user.light_horse.amount + user.armored_horse.hp * user.armored_horse.amount

def _get_defense(user: object) -> int:
    """Védekezés kiszámítása

    Args:
        user (object): Adott felhasználó

    Returns:
        int: Védekezés értéke
    """
    return user.spear_man.defense * user.spear_man.amount + user.sword_man.defense * user.sword_man.amount + user.muskater.defense * user.muskater.amount + user.light_horse.defense * user.light_horse.amount + user.armored_horse.defense * user.armored_horse.amount

def _get_attack(user: object) -> int:
    """Támadás kiszámítása

    Args:
        user (object): Adott felhasználó

    Returns:
        int: Támadás értéke
    """
    return user.spear_man.attack * user.spear_man.amount + user.sword_man.attack * user.sword_man.amount + user.muskater.attack * user.muskater.amount + user.light_horse.attack * user.light_horse.amount + user.armored_horse.attack * user.armored_horse.amount

def _get_summary(attack:int, defense:int) -> int:
    """Egyik támadása és másik védekezéséne különbsége

    Args:
        attack (int): Egyik támadása
        defense (int): Másik védekezése

    Returns:
        int: Egyik összes támadása
    """
    return attack - defense



def Battle(user:object, enemy:object) -> bool:
    """Ez a függvény felelős a csata kimenetének megállapításáért.
    A szabálya az, hogy a hp-t, defense-t és attack-ot összesítve összeveti a másik értékeibel
    és ez alapján kiszámolja ki győzne előbb.

    Képlete:
    <user>_<property> = SZUM(<user>.<unit>.<property> * <user>.<unit>.amount)
    <user>_summary_attack = <user>_attack - <enemyuser>_defense
    <user>_need = <enemyuser>_hp / <user>_summary_attack
    
    Args:
        user (object): A felhasználó adatai.
        enemy (object): Az ellenség adatai.

    Returns:
        bool: Érték mely visszaadja a csata kimenetelét True = felhasználó nyert, False = ellenség nyert.
    """
    user_need = _get_hp(enemy) / exception.is_null(_get_summary(_get_attack(user), _get_defense(enemy)))
    enemy_need = _get_hp(enemy) / exception.is_null(_get_summary(_get_attack(enemy), _get_defense(user)))
    return user_need > enemy_need