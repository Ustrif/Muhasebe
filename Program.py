import sys
from PyQt5.QtWidgets import QPushButton,QVBoxLayout,QAction,QComboBox,qApp,QMainWindow,QLabel,QLineEdit,QWidget,QApplication,QHBoxLayout
from PyQt5 import QtGui
import sqlite3


class MusteriEkle(QWidget):
    def __init__(self):
        super().__init__()
        self.baglan()
        self.urunler()
        self.init_ui()

    def baglan(self):
        txt = sqlite3.connect("veri.db")
        self.cursor = txt.cursor()
        self.cursor.execute("Create Table If not Exists müşteriler (ad TEXT,ürün TEXT,adet INT)")
        txt.commit()

    def urunler(self):
        pyyy = sqlite3.connect("veri.db")
        self.cursor = pyyy.cursor()
        self.cursor.execute("Create Table If not Exists ürünler (Marka TEXT,Adet INT)")
        pyyy.commit()
        pyyy.close()

    def init_ui(self):
        self.adaminadı_ad = QLabel("Ad : ")
        self.adaminadı = QLineEdit()

        self.model_ad = QLabel("Ürünler : ")
        self.kutuseysi = QComboBox(self)
        self.kutuseysi.addItem("İphone X")
        self.kutuseysi.addItem("Huawei P30 Pro")
        self.kutuseysi.addItem("Samsung A80")
        self.kutuseysi.addItem("Xiaomi Mİ 9T")

        self.adet_ad = QLabel("Adet : ")
        self.adet = QLineEdit()

        self.hata = QLabel("")
        self.kayit = QPushButton("Kaydet")

        vbox = QVBoxLayout()

        vbox.addWidget(self.adaminadı_ad)
        vbox.addWidget(self.adaminadı)

        vbox.addWidget(self.model_ad)
        vbox.addWidget(self.kutuseysi)

        vbox.addWidget(self.adet_ad)
        vbox.addWidget(self.adet)

        vbox.addWidget(self.hata)
        vbox.addWidget(self.kayit)

        self.setLayout(vbox)

        self.setWindowTitle("Müşteri Ekleme Ekranı")

        self.kayit.clicked.connect(self.taklama)

    def taklama(self):

        if self.kutuseysi.currentText() == "İphone X":

            ad87 = self.adaminadı.text()
            adt3 = self.adet.text()
            ooooo = "İphone X"

            rtr = sqlite3.connect("veri.db")

            self.cursor = rtr.cursor()

            self.cursor.execute("INSERT INTO müşteriler Values(?,?,?)", (ad87, ooooo, adt3))

            self.hata.setText("Gönderim için beklemede.")

            rtr.commit()
            rtr.close()

        elif self.kutuseysi.currentText() == "Huawei P30 Pro":


            ad87 = self.adaminadı.text()
            adt3 = self.adet.text()
            ooaao = "Huawei P30 Pro"

            rte = sqlite3.connect("veri.db")

            self.cursor = rte.cursor()

            self.cursor.execute("INSERT INTO müşteriler Values(?,?,?)", (ad87,ooaao,adt3))

            self.hata.setText("Gönderim için beklemede.")

            rte.commit()
            rte.close()

        elif self.kutuseysi.currentText() == "Samsung A80":

            ad87 = self.adaminadı.text()
            adt3 = self.adet.text()
            ooooo = "Samsung A80"

            rbsb = sqlite3.connect("veri.db")

            self.cursor = rbsb.cursor()

            self.cursor.execute("INSERT INTO müşteriler Values(?,?,?)", (ad87,ooooo,adt3))

            self.hata.setText("Gönderim için beklemede.")

            rbsb.commit()
            rbsb.close()


        else :
            ad87 = self.adaminadı.text()
            adt3 = self.adet.text()
            otoypssxo = "Xiaomi Mi 9T"

            rtvb = sqlite3.connect("veri.db")

            self.cursor = rtvb.cursor()

            self.cursor.execute("INSERT INTO müşteriler Values(?,?,?)", (ad87, otoypssxo, adt3))

            self.hata.setText("Gönderim için beklemede.")

            rtvb.commit()
            rtvb.close()

class Mussil(QWidget):
    def __init__(self):
        super().__init__()

        self.initui()

    def initui(self):
        self.atnat = QLabel("Silinecek Müşteri'nin Adı : ")
        self.silme = QComboBox(self)

        pors = sqlite3.connect("veri.db")
        self.cursor = pors.cursor()
        self.cursor.execute("Select ad From müşteriler")
        liste32 = self.cursor.fetchall()

        for y in liste32:
            self.silme.addItems(y)



        self.nat = QLabel()
        self.buyyon = QPushButton("Sil")

        vbox = QVBoxLayout()
        vbox.addWidget(self.atnat)
        vbox.addWidget(self.silme)
        vbox.addWidget(self.nat)
        vbox.addWidget(self.buyyon)

        self.setLayout(vbox)

        self.setWindowTitle("Müşteri Silme Ekranı")

        self.buyyon.clicked.connect(self.otpst)

    def otpst(self):

        ad8ısc7 = self.silme.currentText()

        atko = sqlite3.connect("veri.db")

        self.cursor = atko.cursor()

        atko.execute("Delete From müşteriler where ad = ?", (ad8ısc7,))

        self.nat.setText("Silindi.")

        atko.commit()

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pencerea = Notepad()

        self.setCentralWidget(self.pencerea)

        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        musteri = menubar.addMenu("Müşteri")
        urun = menubar.addMenu("Ürün")
        ben = menubar.addMenu("Hakkımda")

        cik = QAction("Çıkış",self)
        cik.setShortcut("ctrl+q")
        dosya.addAction(cik)

        benl = QAction("Hakkımda",self)
        ben.addAction(benl)


        musteri_ekle = QAction("Müşteri Ekle",self)
        musteri_ekle.setShortcut("ctrl+a")
        musteri.addAction(musteri_ekle)

        urun_add = QAction("Ürün Ekle",self)
        urun_add.setShortcut("ctrl+k")
        urun.addAction(urun_add)


        musterisil = QAction("Müşteri Sil",self)
        musterisil.setShortcut("ctrl+d")
        musteri.addAction(musterisil)

        gurun = QAction("Ürünü Gönder",self)
        gurun.setShortcut("Ctrl+G")
        urun.addAction(gurun)

        cik.triggered.connect(self.cks)
        musteri_ekle.triggered.connect(self.addMuster)
        musterisil.triggered.connect(self.deletems)
        urun_add.triggered.connect(self.uraa)
        gurun.triggered.connect(self.yksvla)
        benl.triggered.connect(self.hakkn)

        self.setGeometry(300,100,400,300)
        self.setWindowTitle("Muhasebe")

    def hakkn(self):
        hros.show()
    def cks(self):
        qApp.quit()

    def addMuster(self):
        aaaa.show()

    def deletems(self):
        altab.show()

    def uraa(self):
        uygap.show()

    def yksvla(self):

        okac.show()

class urunekle(QWidget):
    def __init__(self):
        super().__init__()

        self.aop()

    def aop(self):
        self.urunsec_ad = QLabel("Ürün Markası :")
        self.urunsec = QComboBox(self)
        self.phs = "İphone X"
        self.ojs = "Huawei P30 Pro"
        self.skf = "Samsung A80"
        self.mks = "Xiaomi 9T"
        self.urunsec.addItem(self.phs)
        self.urunsec.addItem(self.ojs)
        self.urunsec.addItem(self.skf)
        self.urunsec.addItem(self.mks)

        self.alim_add = QLabel("Ürün Adedi :")
        self.alim = QLineEdit()
        self.httt = QLabel("")
        self.kkkk = QPushButton("Kaydet")

        v_box = QVBoxLayout()

        v_box.addWidget(self.urunsec_ad)
        v_box.addWidget(self.urunsec)
        v_box.addWidget(self.alim_add)
        v_box.addWidget(self.alim)
        v_box.addWidget(self.httt)
        v_box.addWidget(self.kkkk)

        self.setLayout(v_box)
        self.setWindowTitle("Ürün Ekleme")
        self.kkkk.clicked.connect(self.tkland)

    def tkland(self):

        aq = sqlite3.connect("veri.db")
        self.cursor = aq.cursor()
        self.cursor.execute("Create Table If Not Exists ürünler (Marka TEXT,Adet INT)")
        self.adeee = self.alim.text()

        if self.urunsec.currentText() == "İphone X":
            lopsva = "İphone X"

            self.cursor.execute("Insert Into ürünler Values(?,?)",(lopsva,self.adeee))
            self.httt.setText("Eklendi. +++ ")

            self.urunsec.removeItem(0)


        elif self.urunsec.currentText() == "Huawei P30 Pro":
            usva = "Huawei P30 Pro"

            self.cursor.execute("Insert Into ürünler Values(?,?)",(usva,self.adeee))
            self.httt.setText("Eklendi. +++ ")

            self.urunsec.removeItem(1)


        elif self.urunsec.currentText() == "Samsung A80" :
            opas = "Samsung A80"

            self.cursor.execute("Insert Into ürünler Values(?,?)", (opas, self.adeee))
            self.httt.setText("Eklendi. +++ ")

            self.urunsec.removeItem(2)


        else :
            obks = "Xiaomi 9T"

            self.cursor.execute("Insert Into ürünler Values(?,?)",(obks,self.adeee,))
            self.httt.setText("Eklendi. +++ ")

            self.urunsec.removeItem(3)

        aq.commit()
        aq.close()

class ugonder(QWidget):
    def __init__(self):

        super().__init__()

        self.cls()

    def cls(self):
        lars = sqlite3.connect("veri.db")
        self.cursor = lars.cursor()
        self.cursor.execute("Select ad From müşteriler")
        kayra = self.cursor.fetchall()

        self.muaddaaa = QLabel("Gönderim Adı : ")
        self.muadı = QComboBox(self)
        for i in kayra:
            self.muadı.addItems(i)
        self.gunderıldı = QLabel("")
        self.gunder = QPushButton("Ürünü Gönder")


        vbox = QVBoxLayout()
        vbox.addWidget(self.muaddaaa)
        vbox.addWidget(self.muadı)
        vbox.addWidget(self.gunderıldı)
        vbox.addWidget(self.gunder)


        self.setLayout(vbox)
        self.setWindowTitle("Ürünü Gönder!")

        self.gunder.clicked.connect(self.atbaka)

    def atbaka(self):

        vayqa = self.muadı.currentText()

        yars = sqlite3.connect("veri.db")
        self.cursor = yars.cursor()

        self.cursor.execute("Select ürün From müşteriler where ad = ?",(vayqa,))
        lapya = self.cursor.fetchall()

        self.cursor.execute("Select adet From müşteriler where ad = ?", (vayqa,))
        yapya = self.cursor.fetchall()

        dege1 = [('İphone X',)]
        deger1 = "İphone X"

        dege2 = [('Huawei P30 Pro',)]
        deger2 = "Huawei P30 Pro"

        dege3 = [('Samsung A80',)]
        deger3 = "Samsung A80"

        dege4 = [('Xiaomi 9T')]
        deger4 = "Xiaomi 9T"

        if lapya == dege1 :

            ars = sqlite3.connect("veri.db")
            self.cursor = ars.cursor()
            self.cursor.execute("Select Marka From ürünler where Marka = ?",(deger1,))
            oyta1 = self.cursor.fetchall()



            self.cursor.execute("Select Adet from ürünler where Marka = ?",(deger1,))
            okta1 = self.cursor.fetchall()


            if oyta1 != dege1 :
                self.gunderıldı.setText("Böyle ürün yok.")

            elif okta1 < yapya:
                self.gunderıldı.setText("Bu kadar ürün yok.")

            elif oyta1 == dege1 and okta1 > yapya:

                fark = okta1[0][0] - yapya[0][0]

                self.cursor.execute("Delete From müşteriler where ad = ?", (vayqa,))
                self.cursor.execute("Delete From ürünler where Marka = ?",(deger1,))
                self.cursor.execute("Insert Into ürünler Values (?,?)", (deger1, fark,))
                ars.commit()
                self.gunderıldı.setText("Ürünler gönderildi!")

            else:
                self.gunderıldı.setText("Bir şekilde hata oldu.")

        elif lapya == dege2 :

            ars = sqlite3.connect("veri.db")
            self.cursor = ars.cursor()
            self.cursor.execute("Select Marka From ürünler where Marka = ?",(deger2,))
            oyta1 = self.cursor.fetchall()

            self.cursor.execute("Select Adet from ürünler where Marka = ?",(deger2,))
            okta1 = self.cursor.fetchall()


            if oyta1 != dege2 :
                self.gunderıldı.setText("Böyle ürün yok.")

            elif okta1 < yapya:
                self.gunderıldı.setText("Bu kadar ürün yok.")

            elif oyta1 == dege2 and okta1 > yapya:

                fark1 = okta1[0][0] - yapya[0][0]

                self.cursor.execute("Delete From müşteriler where ad = ?", (vayqa,))
                self.cursor.execute("Delete From ürünler where Marka = ?",(deger2,))
                self.cursor.execute("Insert Into ürünler Values (?,?)", (deger2, fark1,))
                ars.commit()
                self.gunderıldı.setText("Ürünler gönderildi!")

            else:
                self.gunderıldı.setText("Bir şekilde hata oldu.")

        elif lapya == dege3 :

            ars = sqlite3.connect("veri.db")
            self.cursor = ars.cursor()
            self.cursor.execute("Select Marka From ürünler where Marka = ?",(deger3,))
            oyta1 = self.cursor.fetchall()

            self.cursor.execute("Select Adet from ürünler where Marka = ?",(deger3,))
            okta1 = self.cursor.fetchall()


            if oyta1 != dege3 :
                self.gunderıldı.setText("Böyle ürün yok.")

            elif okta1 < yapya:
                self.gunderıldı.setText("Bu kadar ürün yok.")

            elif oyta1 == dege3 and okta1 > yapya:

                fark3 = okta1[0][0] - yapya[0][0]

                self.cursor.execute("Delete From müşteriler where ad = ?", (vayqa,))
                self.cursor.execute("Delete From ürünler where Marka = ?",(deger3,))
                self.cursor.execute("Insert Into ürünler Values (?,?)", (deger3, fark3,))
                ars.commit()
                self.gunderıldı.setText("Ürünler gönderildi!")

            else:
                self.gunderıldı.setText("Bir şekilde hata oldu.")

        elif lapya == dege4 :

            ars = sqlite3.connect("veri.db")
            self.cursor = ars.cursor()
            self.cursor.execute("Select Marka From ürünler where Marka = ?",(deger4,))
            oyta1 = self.cursor.fetchall()

            self.cursor.execute("Select Adet from ürünler where Marka = ?",(deger4,))
            okta1 = self.cursor.fetchall()


            if oyta1 != dege4 :
                self.gunderıldı.setText("Böyle ürün yok.")

            elif okta1 < yapya:
                self.gunderıldı.setText("Bu kadar ürün yok.")

            elif oyta1 == dege4 and okta1 > yapya:

                fark4 = okta1[0][0] - yapya[0][0]

                self.cursor.execute("Delete From müşteriler where ad = ?", (vayqa,))
                self.cursor.execute("Delete From ürünler where Marka = ?",(deger4,))
                self.cursor.execute("Insert Into ürünler Values (?,?)", (deger4, fark4,))
                ars.commit()
                self.gunderıldı.setText("Ürünler gönderildi!")

            else:
                self.gunderıldı.setText("Bir şekilde hata oldu.")

class giris(QWidget):
    def __init__(self):
        super().__init__()
        self.baglanti_olustur()

        self.init_ui()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("veri.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("Create Table If not exists Üyeler (kullanıcı TEXT,parola TEXT)")
        self.baglanti.commit()

    def init_ui(self):

        self.kullanici_adi = QLineEdit()
        self.parola = QLineEdit()
        self.parola.setEchoMode(QLineEdit.Password)
        self.kullanici_adi.setObjectName("kullanici_adi")
        self.user = QLabel("AD   :")
        self.yazi_alani = QLabel("")
        self.password = QLabel("ŞİFRE :")
        self.giris = QPushButton("Giriş Yap")
        self.kaydol = QPushButton("Kaydol")

        h_box1 = QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.user)
        h_box1.addWidget(self.kullanici_adi)
        h_box1.addStretch()

        h_box2 = QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.password)
        h_box2.addWidget(self.parola)
        h_box2.addStretch()

        h_box3 = QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.yazi_alani)
        h_box3.addStretch()

        h_box4 = QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.giris)
        h_box4.addWidget(self.kaydol)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addStretch()
        v_box.addLayout(h_box4)

        self.user.setFixedSize(35, 20)
        self.password.setFixedSize(35, 20)
        self.kullanici_adi.setFixedSize(120, 20)
        self.parola.setFixedSize(120, 20)

        self.setLayout(v_box)

        self.giris.clicked.connect(self.login)
        self.kaydol.clicked.connect(self.kayit_ol)

        self.setGeometry(300, 100, 200, 200)
        self.setWindowTitle("Muhasebe Giriş Ekranı")

        self.show()

    def login(self):
        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * From Üyeler where kullanıcı = ? and parola = ?", (adi, par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok\nLütfen tekrar deneyin.")
        else:
            self.yazi_alani.setText("Hoş Geldiniz " + adi)
            pencere.show()

    def kayit_ol(self):
        pencere2.show()

class pencere2(QWidget):
    def __init__(self):
        super().__init__()
        self.arayuz()
        self.connect()

    def connect(self):
        self.baglanti2 = sqlite3.connect("veri.db")
        self.cursor = self.baglanti2.cursor()
        self.cursor.execute("Create Table If not exists Üyeler (kullanıcı TEXT,parola TEXT)")
        self.baglanti2.commit()

    def arayuz(self):
        self.ad_label = QLabel("AD   : ")
        self.sifre_label = QLabel("ŞİFRE : ")
        self.ad_line = QLineEdit()
        self.yazi_alani2 = QLabel("")
        self.sifre_line = QLineEdit()
        self.kaydet = QPushButton("Kayıt Et")

        h_box1 = QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.ad_label)
        h_box1.addWidget(self.ad_line)
        h_box1.addStretch()

        h_box2 = QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.sifre_label)
        h_box2.addWidget(self.sifre_line)
        h_box2.addStretch()

        h_box3 = QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.kaydet)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)

        self.setLayout(v_box)

        self.ad_label.setFixedSize(35, 20)
        self.ad_line.setFixedSize(120, 20)
        self.sifre_label.setFixedSize(35, 20)
        self.sifre_line.setFixedSize(120, 20)

        self.setWindowTitle("           KAYIT OL             ")
        self.setFixedSize(200, 200)

        self.kaydet.clicked.connect(self.account)

    def account(self):
        adi2 = self.ad_line.text()
        sifre2 = self.sifre_line.text()

        self.cursor.execute("INSERT into Üyeler Values(?,?)", (adi2, sifre2))
        self.baglanti2.commit()

class hkkkkk(QWidget):

    def __init__(self):
        super().__init__()
        self.yazm = QLabel("Atmaca7887. Bu programın yazarıyım.\nBeni bulmak istiyorsanız;\nhttps://www.turkhackteam.org/members/818472.html")

        vbox = QVBoxLayout()
        vbox.addWidget(self.yazm)
        self.setLayout(vbox)
        self.setWindowTitle("Hakkımda")
        self.setGeometry(300,100,200,150)

class Notepad(QWidget):
    def __init__(self):
        super().__init__()

        self.initui()

    def initui(self):

        self.anayaz = QLabel("Öncelikle Merhabalar,\n\nMuhasebe programına hoşgeldiniz.\n\n- İlk olarak ürün menüsünden ürün ekleyiniz.\n\n- Daha sonra müşteri ekleyebilirsiniz.\n\n- Son olarak ürün gönder yaparak kullanabilirsiniz.\n\nNot1 : Müşteri ekledikten sonra kapatıp açmanız gerekebilir.\n\nNot2 : İyi kullanımlar dilerim.")
        vbox = QVBoxLayout()
        vbox.addWidget(self.anayaz)
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    aaaa = MusteriEkle()
    pencere = Pencere()
    pencere2 = pencere2()
    altab = Mussil()
    uygap = urunekle()
    okac = ugonder()
    okay = giris()
    hros = hkkkkk()
    sys.exit(app.exec_())

