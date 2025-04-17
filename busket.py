#basket.py
from PyQt6 import QtCore, QtGui, QtWidgets


from enter import db_connect

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 375)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(150, 20, 81, 31))
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(parent=Form)
        self.tableView.setGeometry(QtCore.QRect(20, 60, 361, 192))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 270, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 329, 71, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.load_data()
        self.pushButton.clicked.connect(self.export_db)

    def load_data(self):
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("select * from baskets")

        rows = cursor.fetchall()
        model = QtGui.QStandardItemModel()

        if cursor.description:
            head = [col[0] for col in cursor.description]
            model.setHorizontalHeaderLabels(head)

        for row in rows:
            model.appendRow([QtGui.QStandardItem(str(item)) for item in row])
        self.tableView.setModel(model)
        conn.close()

    def export_db(self):
        model = self.tableView.model()
        open("Корзина.csv", "w", encoding="utf-8").write(
            "\n".join([",".join([str(model.index(r, c).data()) for c in range(model.columnCount())]) for r in range(model.rowCount())])
        )


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Корзина"))
        self.pushButton.setText(_translate("Form", "оформить заказ"))
        self.pushButton_2.setText(_translate("Form", "назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
