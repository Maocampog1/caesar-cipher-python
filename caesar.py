# caesar.py

def _shift_char(ch: str, key: int) -> str:
    """Desplaza letras A-Z/a-z con llave key. Otros caracteres se dejan igual."""
    if not ch.isalpha():
        return ch

    key = key % 26
    base = ord('A') if ch.isupper() else ord('a')
    pos = ord(ch) - base
    return chr(base + ((pos + key) % 26))


def caesar_encrypt(text: str, key: int) -> str:
    """Cifra usando César con llave numérica."""
    return "".join(_shift_char(ch, key) for ch in text)


def caesar_decrypt(text: str, key: int) -> str:
    """Descifra usando César con llave numérica."""
    return caesar_encrypt(text, -key)
