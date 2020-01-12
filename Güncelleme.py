class Musg(QWidget):
    def __init__(self):
        super().__init__()
        self.kalpa()

    def kalpa(self):
        oposvna = sqlite3.connect("veri.db")
        self.cursor = oposvna.cursor()
        self.cursor.execute("Select ad From müşteriler")
        liste = self.cursor.fetchall()

        self.adig_a = QLabel("Değiştirilecek Müşterinin Adı : ")
        self.adig = QComboBox(self)

        for i in liste:
            self.adig.addItems(i)


        self.urun_a = QLabel("Değiştirilecek Ürün : ")
        self.urun = QComboBox(self)
        self.urun.addItem("İphone X")
        self.urun.addItem("Huawei P30 Pro")
        self.urun.addItem("Samsung A80")
        self.urun.addItem("Xiaomi Mİ 9T")


        self.adet_a = QLabel("Değiştirilecek Ürün Adedi : ")
        self.adet = QLineEdit()
        self.atya = QPushButton("Kaydet")

        vbox = QVBoxLayout()
        vbox.addWidget(self.adig_a)
        vbox.addWidget(self.adig)
        vbox.addWidget(self.urun_a)
        vbox.addWidget(self.urun)
        vbox.addWidget(self.adet_a)
        vbox.addWidget(self.adet)
        vbox.addWidget(self.atya)

        self.setLayout(vbox)

        self.setWindowTitle("Müşteri Güncelleme Ekranı")

        self.atya.clicked.connect(self.atabet)

    def atabet(self):

        kelime = self.adet.text()

        if self.urun.currentText() == "İphone X" :
            iphonex = "İphone X"
            con = sqlite3.connect("veri.db")

            self.cursor = con.cursor()
            self.cursor.execute("Update müşteriler set ürün = ?", (iphonex))
            self.cursor.execute("Update müşteriler set adet = ?",(kelime))
            con.commit()

        elif self.urun.currentText() == "Huawei P30 Pro" :

            huaweix = "Huawei P30 Pro"
            con = sqlite3.connect("veri.db")

            self.cursor = con.cursor()
            self.cursor.execute("Update müşteriler set ürün = ? ", (huaweix))
            self.cursor.execute("Update müşteriler set adet = ?", (kelime))
            con.commit()

        elif self.urun.currentText() == "Samsung A80" :

            samsung = "Samsung A80"
            con = sqlite3.connect("veri.db")

            self.cursor = con.cursor()
            self.cursor.execute("Update müşteriler set ürün = ? ", (samsung))
            self.cursor.execute("Update müşteriler set adet = ?", (kelime))
            con.commit()

        else :
            xiaomi = "Xiaomi 9T"
            con = sqlite3.connect("veri.db")

            self.cursor = con.cursor()
            self.cursor.execute("Update müşteriler set ürün = ? ", (xiaomi))
            self.cursor.execute("Update müşteriler set adet = ?", (kelime))
            con.commit()


