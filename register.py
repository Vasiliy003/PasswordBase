from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import json
from hashlib import sha256
from good_cypher import encrypt, generate_key
import debug


class Register():
    def __init__(self):
        Form, Window = uic.loadUiType("Register.ui")
        with open("sign_base.json", "r") as f:
            self.data = json.load(f)
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)
        self.form.register_button.clicked.connect(self.register_btn_click)
        self.debug_window = debug.Debug()

    def debug_window_show(self, text):
        self.debug_window.show_window()
        self.debug_window.load_data(text)

    def register_btn_click(self):
        login = self.form.login_input.text()
        password = self.form.password_input.text()
        hash_password = sha256(password.encode("utf-8")).hexdigest()
        check_pass = self.form.check_password_input.text()
        if password != check_pass:
            self.debug_window_show("Пароли не совпадают")
            return
        elif login in self.data:
            self.debug_window_show("Логин уже занят")
            return
        else:

            encrypt(f"{login}_db.json", generate_key(password, login), [])
            account_info = {"password_hash": hash_password, "file_name": f"{login}_db.json"}
            self.data[login] = account_info
            with open("sign_base.json", "w") as g:
                json.dump(self.data, g)
            print("Пользователь успешно зарегестрирован")
            self.window.hide()

    def show_window(self):
        self.window.show()

    def close_window(self):
        self.window.close()


if __name__ == "__main__":
    app = QApplication([])
    register_window = Register()
    register_window.show_window()

    app.exec()
