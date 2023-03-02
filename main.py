from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import json
from PyQt5 import QtCore
import random


class Main():
    def __init__(self):
        Form, Window = uic.loadUiType("Main.ui")
        try:
            with open("password_base.json", "r") as f:
                self.data = json.load(f)
        except Exception:
            self.data = []
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)
        self.form.add_password_btn.clicked.connect(self.new_password_add)
        self.table_init()
        self.form.Random_password_btn.clicked.connect(self.random_password_btn)
        self.form.Tabs.keyPressEvent = self.key_press_event

    def key_press_event(self, key):
        if key.key() == 16777223 and self.form.Tabs.currentIndex() == 0:
            row = self.form.tableWidget.currentRow()
            del self.data[row - 1]
            with open("password_base.json", "w") as g:
                json.dump(self.data, g)
            self.form.tableWidget.removeRow(row)

    def random_password_btn(self):
        password = ""
        numbers = "0123456789"
        high_latter = "QWERTYUIOPASDFGHJKLZXCVBNM"
        lower_latter = "qwertyuiopasdfghjklzxcvbnm"
        chars = "!@#$%^&*()+=-:;№"
        for i in range(2):
            password += random.choice(numbers)
            password += random.choice(high_latter)
            password += random.choice(lower_latter)
            password += random.choice(chars)
        self.form.password_input.setText(password)
        self.form.check_password_input.setText(password)

    def table_init(self):
        self.form.tableWidget.setRowCount(len(self.data) + 1)
        for i in range(1, 3):
            self.form.tableWidget.setColumnWidth(i, 150)
        self.form.tableWidget.setColumnWidth(0, 100)
        self.form.tableWidget.setColumnWidth(3, 300)
        self.form.tableWidget.setHorizontalHeaderLabels(["Сервис", "Логин", "Пароль", "Заметка"])
        for i in range(len(self.data)):
            site_item = QTableWidgetItem(self.data[i][0])
            site_item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            login_item = QTableWidgetItem(self.data[i][1]["login"])
            login_item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            password_item = QTableWidgetItem(self.data[i][1]["password"])
            password_item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            note_item = QTableWidgetItem(self.data[i][1]["note"])
            note_item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.form.tableWidget.setItem(i, 0, site_item)
            self.form.tableWidget.setItem(i, 1, login_item)
            self.form.tableWidget.setItem(i, 2, password_item)
            self.form.tableWidget.setItem(i, 3, note_item)

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
            self.data.append([site, site_info])
            with open("password_base.json", "w") as g:
                json.dump(self.data, g)
            print("Пароль был успешно добавлен в базу данных")
            return

    def show_window(self, current_account):
        self.window.show()
        print(current_account)

    def close_window(self):
        self.window.close()


if __name__ == "__main__":
    app = QApplication([])
    main_window = Main()
    main_window.show_window()

    app.exec()
