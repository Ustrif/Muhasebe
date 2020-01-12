import sys
from PyQt5 import QtWidgets
import sqlite3

class giris(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.baglan()

        self.init_ui()
    def baglan(self):
        baglan = sqlite3.connect("veri.db")

        self.cursor = baglan.cursor()

        self.cursor.execute("Create Table If not Exists Üyeler (kullanıcı TEXT,parola TEXT)")

        baglan.commit()

    def init_ui(self):

        self.kadı = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.yazı = QtWidgets.QLabel("")
        self.kayıt = QtWidgets.QPushButton("Kayıt ol!")
        self.gir = QtWidgets.QPushButton("Giriş!")
        self.yazı = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kadı)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazı)
        v_box.addStretch()
        v_box.addWidget(self.kayıt)
        v_box.addWidget(self.gir)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.setWindowTitle("Muhasebe Giriş")
        self.gir.clicked.connect(self.login)
        self.kayıt.clicked.connect(self.register)
        self.show()

    def login(self):

        isim = self.kadı.text()
        par = self.parola.text()

        self.cursor.execute("Select * From Üyeler where kullanıcı = ? and parola = ?",(isim,par))
        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazı.setText("Böyle bir kullanıcı yok\nLütfen tekrar deneyin.")
        else :
            self.yazı.setText("Giriş Başarılı!")

    def register(self):

        ad = self.kadı.text()
        sıf = self.parola.text()

        rrr = sqlite3.connect("veri.db")

        self.cursor = rrr.cursor()

        self.cursor.execute("INSERT INTO Üyeler Values(?,?)",(ad,sıf))

        rrr.commit()
        self.yazı.setText("Kayıt olundu!")


app = QtWidgets.QApplication(sys.argv)

okay = giris()

sys.exit(app.exec_())
