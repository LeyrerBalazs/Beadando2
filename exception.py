import userhanding

def _is_same_password(password1:str, password2:str) -> bool:
    return password1 == password2

def _isnt_same_user(username:str) -> bool:
    users = userhanding._load_users()
    allow = True
    for us in users:
        if us == username:
            allow = False
    return allow

def _is_same_user(username:str, user:str) -> bool:
    return username == user