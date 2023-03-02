from cryptography.fernet import Fernet
import base64


def generate_key(password, login):
    passlogin = password + login
    key = passlogin.encode("utf-8")

    if len(key) < 32:
        my_key = base64.urlsafe_b64encode(key[:32])
    else:
        my_key = base64.urlsafe_b64encode(key + b"0" * (32 - len(key)))
    return my_key
