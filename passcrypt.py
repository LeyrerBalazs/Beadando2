def caesar(password:str) -> str:
    """Ez a függvény felel, hogy ne plaintext-be tárolodjon az adat, így egy caesar titkosítás
    szerű titkosítást használ.

    Args:
        password (str): A felhasználó jelszava plaintextben.

    Returns:
        str: A felhasználó jelszava letitkosítva.
    """
    return [chr(ord(char) + 4) for char in password]