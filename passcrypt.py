def caesar(password:str) -> str:
    encrypted = ""
    for char in password:
        binary = ord(char) + 4
        encrypted += chr(binary)
    return encrypted