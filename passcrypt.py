def caesar(password:str) -> str:
    """Ez a függvény felel, hogy ne plaintext-be tárolodjon az adat, így egy caesar titkosítás
    szerű titkosítást használ.

    Args:
        password (str): A felhasználó jelszava plaintextben.

    Returns:
        str: A felhasználó jelszava letitkosítva.
    """
    encrypted = ""
    for char in password:
        binary = ord(char) + 4
        encrypted += chr(binary)
    return encrypted