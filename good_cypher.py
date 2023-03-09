from cryptography.fernet import Fernet
import base64


def generate_key(password, login):
    passlogin = password + login
    key = passlogin.encode("utf-8")
    print(len(key))

    if len(key) < 32:
        my_key = base64.urlsafe_b64encode(key[:32])
    else:
        my_key = base64.urlsafe_b64encode(key + b"0" * (32 - len(key)))
    return my_key


def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as g:
        file_data = g.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as g:
        g.write(encrypted_data)


print(encrypt("Georgia_db.json", generate_key("1", "gg")))