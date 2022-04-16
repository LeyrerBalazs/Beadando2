import exception, user, pickle, os, passcrypt

def _register(username:str, password1:str, password2:str) -> bool:
    if exception._isnt_same_user(username) and exception._is_same_password(password1, password2):
        u = user.User_save(username, password1)
        fajl = open(f'users/{username}.obj', "wb")
        pickle.dump(u, fajl)
        fajl.close()
        return True
    else:
        return False

def _load_users() -> list:
    userfiles = os.listdir("./users")
    users = []
    for userinfile in userfiles:
        users.append(os.path.splitext(userinfile)[0])
    return users

def _login(username, password) -> bool:
    is_same = False
    for user in _load_users():
        if exception._is_same_user(username = username, user = user):
            is_same = True
    if is_same:
        file = open(f'./users/{username}.obj', "rb")
        u = pickle.load(file)
        file.close()
        if exception._is_same_password(password1=u.password, password2=passcrypt.caesar(password)):
            return True
        else:
            return False
    else:
        return False

def _save_user(user:object) -> None:
    fajl = open(f'users/{user.name}.obj', "wb")
    pickle.dump(user, fajl)
    fajl.close()