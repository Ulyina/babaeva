        self.comboBox_populate1()
        self.comboBox_populate2()
        self.comboBox_populate3()
        self.pushButton.clicked.connect(self.insert_v)
        self.pushButton_2.clicked.connect(self.open_basket)
        self.pushButton_3.clicked.connect(self.open_cus)
        self.pushButton_3.clicked.connect(Form.close)

    def comboBox_populate1(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT material FROM carpets")
        for material in cursor.fetchall():
            self.comboBox.addItem(material[0])
        if conn:
            conn.close()

    def comboBox_populate2(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT country_of_origin FROM carpets")
        for country_of_origin in cursor.fetchall():
            self.comboBox_2.addItem(country_of_origin[0])
        if conn:
            conn.close()

    def comboBox_populate3(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT model_name FROM carpets")
        for model_name in cursor.fetchall():
            self.comboBox_3.addItem(model_name[0])
        if conn:
            conn.close()

    def insert_v(self):

        name_model_v = self.comboBox_3.currentText()
        name_material_v = self.comboBox.currentText()
        name_country_v = self.comboBox_2.currentText()
        lenght_v = int(self.lineEdit.text())
        hieght_v = int(self.lineEdit_2.text())

        conn = db_connection()
        cursor = conn.cursor()
        sql = """INSERT INTO basket (name_model, name_material, name_country, lenght, hieght)
                VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (name_model_v, name_material_v, name_country_v, lenght_v, hieght_v))
        conn.commit()

        QtWidgets.QMessageBox.information(None, "Успех", "Заказ успешно создан!")
        if conn:
            conn.close()
