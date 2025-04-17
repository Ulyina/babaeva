#manager.py


from PyQt6 import QtCore, QtGui, QtWidgets
from enter import db_connect

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 344)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(100, 30, 171, 31))
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(parent=Form)
        self.tableView.setGeometry(QtCore.QRect(30, 70, 341, 192))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 290, 81, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.load_data()

        self.pushButton.clicked.connect(self.open_enter)
        self.pushButton.clicked.connect(Form.close)

    def load_data(self):
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("select * from orders")
        rows = cursor.fetchall()

        model = QtGui.QStandardItemModel()
        if cursor.description:
            headers = [col[0] for col in cursor.description]
            model.setHorizontalHeaderLabels(headers)

        for row in rows:
            model.appendRow([QtGui.QStandardItem(str(item)) for item in row])
        self.tableView.setModel(model)

        conn.close()

    def open_enter(self):
        from enter import Ui_Form
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.win)
        self.win.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ЗАКАЗЫ"))
        self.pushButton.setText(_translate("Form", "НАЗАД"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
