from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("UI.ui")


def sign_click():
    print(form.loginInput.text())


def show_password():
    state = form.passwordShow.isChecked()
    if state:
        form.passwordInput.setEchoMode(0)
    else:
        form.passwordInput.setEchoMode(2)


attempts = 3


def check_log_pass():
    global attempts
    login = form.loginInput.text()
    password = form.passwordInput.text()
    if login == "Georgia" and password == "180923":
        print("Успешно!")
        exit()
    else:
        if attempts <= 1:
            print("У вас закончились попытки для входа в систему. Попробуйте позже (никогда)")
            exit()
        else:
            attempts -= 1
            print(f"Неверный логин или пароль. У вас осталось {str(attempts)} попыток!")


app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

form.sign.clicked.connect(check_log_pass)
form.passwordShow.stateChanged.connect(show_password)

app.exec()