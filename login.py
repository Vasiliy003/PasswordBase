from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import json
from hashlib import sha256
import register
import main
import debug
from good_cypher import generate_key


class Login():
    def __init__(self):
        Form, Window = uic.loadUiType("UI.ui")
        with open("sign_base.json", "r") as f:
            self.data = json.load(f)
        self.attempts = 3
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)
        self.register_window = register.Register()
        self.main_window = main.Main()
        self.debug_window = debug.Debug()
        self.form.sign.clicked.connect(self.check_log_pass)
        self.form.passwordShow.stateChanged.connect(self.show_password)
        self.form.register_acc_btn.clicked.connect(self.register_click)

    def debug_window_show(self, text):
        self.debug_window.show_window()
        self.debug_window.load_data(text)

    def register_click(self):
        self.register_window.show_window()
        self.window.hide()

    def main_start(self):
        password = self.form.passwordInput.text()
        login = self.form.loginInput.text()
        self.main_window.show_window()
        self.main_window.load_data({"login": login, "password": password})
        self.window.hide()

    def show_password(self):
        state = self.form.passwordShow.isChecked()
        if state:
            self.form.passwordInput.setEchoMode(0)
        else:
            self.form.passwordInput.setEchoMode(2)

    def check_log_pass(self):
        login = self.form.loginInput.text()
        password = self.form.passwordInput.text()
        password_hash = sha256(password.encode("utf-8")).hexdigest()
        if login in self.data and self.data[login]["password_hash"] == password_hash:
            self.main_start()
        else:
            if self.attempts <= 1:
                pass
                #self.debug_window_show("У вас закончились попытки для входа в систему. Попробуйте позже (никогда)")
                exit()

            else:
                self.attempts -= 1
                self.debug_window_show(f"Неверный логин или пароль. У вас осталось {str(self.attempts)} попыток!")

    def show_window(self):
        self.window.show()

    def close_window(self):
        self.window.close()



if __name__ == "__main__":
    app = QApplication([])
    login_window = Login()
    login_window.show_window()

    app.exec()