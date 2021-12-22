from PyQt5 import QtWidgets, QtGui
import sys
import requests

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Məzənnə kalkulyatoru")
        self.setMaximumSize(450, 200)
        self.setMinimumSize(450, 200)
        self.setWindowIcon(QtGui.QIcon("images/istockphoto-1217946228-612x612.jpg"))
        self.init_ui()

    def init_ui(self):
        yazi_alani = QtWidgets.QLabel("Məzənnə kalkulyatoru")
        yazi_alani.setFont(QtGui.QFont("Calibri", 14))
        foto = QtWidgets.QLabel()
        foto.setPixmap(QtGui.QPixmap("images/para.jpg"))
        self.comboBox1 = QtWidgets.QComboBox()
        para_birimi = ["...", "AZN", "TRY", "USD", "EUR"]
        self.comboBox1.addItems(para_birimi)
        self.comboBox2 = QtWidgets.QComboBox()
        self.comboBox2.addItems(para_birimi)
        self.spinBox = QtWidgets.QDoubleSpinBox()
        self.spinBox.setRange(0, 999999999999)
        self.yazi = QtWidgets.QLabel("")

        hBox = QtWidgets.QHBoxLayout()
        hBox.addWidget(yazi_alani)
        hBox.addWidget(foto)

        hBox1 = QtWidgets.QHBoxLayout()
        hBox1.addWidget(self.spinBox)
        hBox1.addWidget(self.comboBox1)

        hBox2 = QtWidgets.QHBoxLayout()
        hBox2.addWidget(self.yazi)
        hBox2.addWidget(self.comboBox2)

        vBox = QtWidgets.QVBoxLayout()
        vBox.addLayout(hBox)
        vBox.addLayout(hBox1)
        vBox.addLayout(hBox2)


        self.comboBox1.activated.connect(self.click)
        self.comboBox2.activated.connect(self.click)
        self.spinBox.valueChanged.connect(self.click)

        self.setLayout(vBox)
        self.show()


    def click(self):
        text1 = str(self.comboBox1.currentText())
        text2 = str(self.comboBox2.currentText())
        rakam = self.spinBox.value()
        json_iceriyi = self.icerik()
        azn = json_iceriyi["rates"]["AZN"]
        usd = json_iceriyi["rates"]["USD"]
        tl = json_iceriyi["rates"]["TRY"]
        eur = json_iceriyi["rates"]["EUR"]

        if text1 == "USD" and text2 == "AZN":
            hesaplama = str((azn / usd) * rakam)
            self.yazi.setText(hesaplama)
        elif text1 == "AZN" and text2 == "USD":
            hesaplama = str((usd / azn) * rakam)
            self.yazi.setText(hesaplama)

        elif text1 == "TRY" and text2 == "AZN":
            hesaplama = str((azn / tl) * rakam)
            self.yazi.setText(hesaplama)
        elif text1 == "AZN" and text2 == "TRY":
            hesaplama = str((tl / azn) * rakam)
            self.yazi.setText(hesaplama)

        elif text1 == "EUR" and text2 == "AZN":
            hesaplama = str((azn / eur) * rakam)
            self.yazi.setText(hesaplama)
        elif text1 == "AZN" and text2 == "EUR":
            hesaplama = str((eur / azn) * rakam)
            self.yazi.setText(hesaplama)

        elif text1 == "EUR" and text2 == "TRY":
            hesaplama = str((tl / eur) * rakam)
            self.yazi.setText(hesaplama)
        elif text1 == "TRY" and text2 == "EUR":
            hesaplama = str((eur / tl) * rakam)
            self.yazi.setText(hesaplama)

        elif text1 == "USD" and text2 == "TRY":
            hesaplama = str((tl / usd) * rakam)
            self.yazi.setText(hesaplama)
        elif text1 == "TRY" and text2 == "USD":
            hesaplama = str((usd / tl) * rakam)
            self.yazi.setText(hesaplama)

        elif text1 == "USD" and text2 == "EUR":
            hesaplama = str((eur / usd) * rakam)
            self.yazi.setText(hesaplama)
        elif text1 == "EUR" and text2 == "USD":
            hesaplama = str((usd / eur) * rakam)
            self.yazi.setText(hesaplama)


    def icerik(self):
        access_key = "-----KEY-----"
        url = "http://data.fixer.io/api/latest?access_key=" + access_key
        response = requests.get(url)
        json_iceriyi = response.json()
        return json_iceriyi



app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
