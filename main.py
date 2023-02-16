from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import json


class Main():
    def __init__(self):
        Form, Window = uic.loadUiType("Main.ui")
        with open("password_base.json", "r") as f:
            self.data = json.load(f)
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)
        self.form.add_password_btn.clicked.connect(self.new_password_add)

    def new_password_add(self):
        site = self.form.site_input.text()
        login = self.form.login_input.text()
        password = self.form.password_input.text()
        check_password = self.form.check_password_input.text()
        note = self.form.note_text.toPlainText()
        if password != check_password:
            print("Пароли не совпадают")
            return
        elif site in self.data:
            print("Сайт уже внесён в базу данных")
            return
        else:
            site_info = {"login": login, "password": password, "note": note}
            self.data[site] = site_info
            with open("password_base.json", "w") as g:
                json.dump(self.data, g)
            print("Пароль был успешно добавлен в базу данных")
            return


    def show_window(self):
        self.window.show()

    def close_window(self):
        self.window.close()


if __name__ == "__main__":
    app = QApplication([])
    main_window = Main()
    main_window.show_window()

    app.exec()
