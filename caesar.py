# caesar.py
# Autor: (pon tu nombre)
# Propósito: Cifrar y descifrar usando el cifrado César con llave numérica.

def _shift_char(ch: str, key: int) -> str:
    """Desplaza una letra manteniendo mayúsculas/minúsculas. No-alfabético se deja igual."""
    if not ch.isalpha():
        return ch

    key = key % 26
    base = ord('A') if ch.isupper() else ord('a')
    offset = ord(ch) - base
    return chr(base + ((offset + key) % 26))


def caesar_encrypt(text: str, key: int) -> str:
    """Cifra un texto con César usando 'key'."""
    return "".join(_shift_char(ch, key) for ch in text)


def caesar_decrypt(text: str, key: int) -> str:
    """Descifra un texto con César usando 'key'."""
    return caesar_encrypt(text, -key)
