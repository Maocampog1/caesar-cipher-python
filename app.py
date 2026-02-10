# app.py
from pyscript import document
from caesar import caesar_encrypt, caesar_decrypt

inp_text = document.querySelector("#inp_text")
inp_key = document.querySelector("#inp_key")
out_text = document.querySelector("#out_text")
btn_encrypt = document.querySelector("#btn_encrypt")
btn_decrypt = document.querySelector("#btn_decrypt")
btn_clear = document.querySelector("#btn_clear")

def get_key() -> int:
    try:
        return int(inp_key.value)
    except Exception:
        return 0

def on_encrypt(event=None):
    k = get_key()
    out_text.value = caesar_encrypt(inp_text.value, k)

def on_decrypt(event=None):
    k = get_key()
    out_text.value = caesar_decrypt(inp_text.value, k)

def on_clear(event=None):
    inp_text.value = ""
    out_text.value = ""

btn_encrypt.addEventListener("click", on_encrypt)
btn_decrypt.addEventListener("click", on_decrypt)
btn_clear.addEventListener("click", on_clear)
