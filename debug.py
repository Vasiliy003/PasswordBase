from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

class Debug():
    def __init__(self):
        Form, Window = uic.loadUiType("Debug.ui")
        self.window = Window()
        self.form = Form()
        self.form.setupUi(self.window)
        self.data = None

    def load_data(self, data):
        self.data = data
        self.form.debug_text.setText(data)

    def show_window(self):
        self.window.show()

    def close_window(self):
        self.window.close()


if __name__ == "__main__":
    app = QApplication([])
    main_window = Debug()
    main_window.show_window()

    app.exec()