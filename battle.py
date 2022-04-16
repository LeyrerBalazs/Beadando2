def _Battle(user:object, enemy:object) -> bool:
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
    user_hp = user.spear_man.hp * user.spear_man.amount + user.sword_man.hp * user.sword_man.amount + user.muskater.hp * user.muskater.amount + user.light_horse.hp * user.light_horse.amount + user.armored_horse.hp * user.armored_horse.amount
    user_defense = user.spear_man.defense * user.spear_man.amount + user.sword_man.defense * user.sword_man.amount + user.muskater.defense * user.muskater.amount + user.light_horse.defense * user.light_horse.amount + user.armored_horse.defense * user.armored_horse.amount
    user_attack = user.spear_man.attack * user.spear_man.amount + user.sword_man.attack * user.sword_man.amount + user.muskater.attack * user.muskater.amount + user.light_horse.attack * user.light_horse.amount + user.armored_horse.attack * user.armored_horse.amount
    enemy_hp = enemy.spear_man.hp * enemy.spear_man.amount + enemy.sword_man.hp * enemy.sword_man.amount + enemy.muskater.hp * enemy.muskater.amount + enemy.light_horse.hp * enemy.light_horse.amount + enemy.armored_horse.hp * enemy.armored_horse.amount
    enemy_defense = enemy.spear_man.defense * enemy.spear_man.amount + enemy.sword_man.defense * enemy.sword_man.amount + enemy.muskater.defense * enemy.muskater.amount + enemy.light_horse.defense * enemy.light_horse.amount + enemy.armored_horse.defense * enemy.armored_horse.amount
    enemy_attack = enemy.spear_man.attack * enemy.spear_man.amount + enemy.sword_man.attack * enemy.sword_man.amount + enemy.muskater.attack * enemy.muskater.amount + enemy.light_horse.attack * enemy.light_horse.amount + enemy.armored_horse.attack * enemy.armored_horse.amount
    user_summary_attack = user_attack - enemy_defense
    enemy_summary_attack = enemy_attack - user_defense
    user_need = enemy_hp / user_summary_attack
    enemy_need = user_hp / enemy_summary_attack
    if user_need > enemy_need:
        return True
    else:
        return False 