from PyQt5 import QtWidgets, QtGui
import sys
import requests

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulyator")
        self.setMaximumSize(500, 240)
        self.setMinimumSize(500, 240)
        self.setWindowIcon(QtGui.QIcon("Images/istockphoto-1217946228-612x612.jpg"))
        self.init_ui()

    def init_ui(self):
        yazi_alani = QtWidgets.QLabel("Məzənnə kalkulyatoru")
        yazi_alani.setFont(QtGui.QFont("Calibri", 14))
        foto = QtWidgets.QLabel()
        foto.setPixmap(QtGui.QPixmap("Images/para.jpg"))
        self.comboBox1 = QtWidgets.QComboBox()
        para_birimi = ["...", "AZN", "TRY", "USD", "EUR"]
        self.comboBox1.addItems(para_birimi)
        self.comboBox2 = QtWidgets.QComboBox()
        self.comboBox2.addItems(para_birimi)
        self.spinBox = QtWidgets.QDoubleSpinBox()
        self.spinBox.setRange(0, 999999999999)
        self.yazi = QtWidgets.QLabel("")
        self.button = QtWidgets.QPushButton("convert")

        hBox = QtWidgets.QHBoxLayout()
        hBox.addWidget(yazi_alani)
        hBox.addWidget(foto)

        hBox1 = QtWidgets.QHBoxLayout()
        hBox1.addWidget(self.spinBox)
        hBox1.addWidget(self.comboBox1)

        hBox2 = QtWidgets.QHBoxLayout()
        hBox2.addWidget(self.yazi)
        hBox2.addWidget(self.comboBox2)

        hBox3 = QtWidgets.QHBoxLayout()
        hBox3.addStretch()
        hBox3.addWidget(self.button)

        vBox = QtWidgets.QVBoxLayout()
        vBox.addLayout(hBox)
        vBox.addLayout(hBox1)
        vBox.addLayout(hBox2)
        vBox.addLayout(hBox3)

        self.button.clicked.connect(self.click)

        self.setLayout(vBox)
        self.show()


    def click(self):
        text1 = str(self.comboBox1.currentText())
        text2 = str(self.comboBox2.currentText())
        rakam = self.spinBox.value()

        answer = self.calculation(text1, text2, rakam)
        self.yazi.setText(answer)

    def icerik(self):
        url = "http://data.fixer.io/api/latest?access_key=88e53423e91194f8428de2874ccb628a"
        response = requests.get(url)
        json_iceriyi = response.json()
        return json_iceriyi

    def calculation(self, text1, text2, num):
        json_iceriyi = self.icerik()
        currency1 = json_iceriyi["rates"][text1]
        currency2 = json_iceriyi["rates"][text2]
        answer = str((currency2 / currency1) * num)
        return answer


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
