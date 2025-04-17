#reg.py

from PyQt6 import QtCore, QtGui, QtWidgets
from enter import db_connect

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 538)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(180, 20, 121, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(60, 130, 221, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 500, 91, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 171, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 210, 221, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 440, 171, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 171, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(60, 260, 171, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 300, 221, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(60, 350, 171, 21))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(60, 380, 221, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.insert_v)
        self.comboBox_populate()
        self.pushButton_2.clicked.connect(self.open_enter)
        self.pushButton_2.clicked.connect(Form.close)



    def comboBox_populate(self):
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("select id_role, name from role")
        for id_role, name in cursor.fetchall():
            self.comboBox.addItem(str(name), id_role)
        conn.close()


    def insert_v(self):
        name_v = self.lineEdit.text()
        login_v = self.lineEdit_2.text()
        password_v = self.lineEdit_3.text()
        role_v = self.comboBox.currentData()

        conn = db_connect()
        cursor = conn.cursor()
        sql = """insert into users (name, login, password, role)
                VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (name_v, login_v, password_v, role_v))

        conn.commit()

        QtWidgets.QMessageBox.information(None, "Успех!", "Пользователь успешно добавлен!")

    def open_enter(self):
        from enter import Ui_Form
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)
        self.win.show()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "РЕГИСТРАЦИЯ"))
        self.pushButton_2.setText(_translate("Form", "НАЗАД"))
        self.label_2.setText(_translate("Form", "ВВЕДИТЕ ИМЯ"))
        self.pushButton.setText(_translate("Form", "ЗАРЕГЕСТРИРОВАТЬСЯ"))
        self.label_3.setText(_translate("Form", "ВВЕДИТЕ ЛОГИН"))
        self.label_4.setText(_translate("Form", "ВВЕДИТЕ ПАРОЛЬ"))
        self.label_5.setText(_translate("Form", "ВЫБЕРИТЕ РОЛЬ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
