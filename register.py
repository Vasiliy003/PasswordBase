from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import json
from hashlib import sha256

Form, Window = uic.loadUiType("Register.ui")
with open("sign_base.json", "r") as f:
    data = json.load(f)


def register_btn():
    global data
    login = form.login_input.text()
    password = form.password_input.text()
    hash_password = sha256(password.encode("utf-8")).hexdigest()

    check_pass = form.check_password_input.text()
    if password != check_pass:
        print("Пароли не совпадают")
        return
    elif login in data:
        print("Логин уже занят")
        return
    else:
        data[login] = hash_password
        with open("sign_base.json", "w") as g:
            json.dump(data, g)
        print("Пользователь успешно зарегестрирован")
        exit()


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


form.register_button.clicked.connect(register_btn)


app.exec()
