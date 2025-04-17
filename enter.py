#enter.py


from PyQt6 import QtCore, QtGui, QtWidgets
import pymysql

current_id_user = None

def db_connect():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="window_bd"
    )

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 402)
        Form.setStyleSheet("background-color: rgb(176, 200, 172);")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(170, 20, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 171, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(50, 130, 221, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 210, 221, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 171, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 270, 71, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 320, 151, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.enter_v)
        self.pushButton.clicked.connect(Form.close)
        self.pushButton_2.clicked.connect(self.open_reg)
        self.pushButton_2.clicked.connect(Form.close)

    def enter_v(self):
        login_v = self.lineEdit.text()
        password_v = self.lineEdit_2.text()

        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("select role, id_user from users where login=%s and password = %s",
                       (login_v, password_v))

        result = cursor.fetchall()
        conn.close()

        if result:
            id_role, user_id = result[0]
            global current_id_user
            current_id_user = user_id  # Устанавливаем ID пользователя
            print(f"Текущий ID пользователя: {current_id_user}")  # Отладочный вывод

            if id_role == 1:
                from client import Ui_Form
                self.win = QtWidgets.QMainWindow()
                self.ui = Ui_Form()
                self.ui.setupUi(self.win)
                self.win.show()
            else:
                from manager import Ui_Form
                self.win = QtWidgets.QMainWindow()
                self.ui = Ui_Form()
                self.ui.setupUi(self.win)
                self.win.show()
        else:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Неверный логин или пароль.")

    def open_reg(self):
        from reg import Ui_Form
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)
        self.win.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ВХОД"))
        self.label_2.setText(_translate("Form", "ВВЕДИТЕ ЛОГИН"))
        self.label_3.setText(_translate("Form", "ВВЕДИТЕ ПАРОЛЬ"))
        self.pushButton.setText(_translate("Form", "ВОЙТИ"))
        self.pushButton_2.setText(_translate("Form", "ЗАРЕГЕСТРИРОВАТЬСЯ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
