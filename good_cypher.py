from cryptography.fernet import Fernet
import base64
from os.path import isfile
import json


def generate_key(password, login):
    passlogin = password + login
    key = passlogin.encode("utf-8")

    if len(key) > 32:
        my_key = base64.urlsafe_b64encode(key[:32])
    else:
        my_key = base64.urlsafe_b64encode(key + b"0" * (32 - len(key)))
    return my_key


def encrypt(filename, key, data):
    if not isfile(filename):
        with open(filename, "w") as g:
            pass

    data = json.dumps(data).encode("utf-8")
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    with open(filename, 'wb') as g:
        g.write(encrypted_data)


def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as g:
        encrypted_data = g.read()
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data

#print(decrypt("Georgia_db.json", generate_key("1", "gg")))