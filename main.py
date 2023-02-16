from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


class Main():
    def __init__(self):
        Form, Window = uic.loadUiType("Main.ui")
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)

    def show_window(self):
        self.window.show()

    def close_window(self):
        self.window.close()


if __name__ == "__main__":
    app = QApplication([])
    main_window = Main()
    main_window.show_window()

    app.exec()
