from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from calc_intrface import Ui_Dialog
from math_logic import Equals, Complex
import math

# create application
app = QtWidgets.QApplication(sys.argv)

# create form and init UI
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# application logic

def Ninput(num):
    pb_n = str(num)
    ui.label_11.setText(ui.label_11.text() + pb_n)

def Delete():
    a = ui.label_11.text()
    a = a[:-1]
    ui.label_11.setText(a)


ui.pushButton.clicked.connect(lambda: Ninput(7))
ui.pushButton_2.clicked.connect(lambda: Ninput(8))
ui.pushButton_3.clicked.connect(lambda: Ninput(9))
ui.pushButton_4.clicked.connect(lambda: Ninput(5))
ui.pushButton_5.clicked.connect(lambda: Ninput(4))
ui.pushButton_6.clicked.connect(lambda: Ninput(1))
ui.pushButton_7.clicked.connect(lambda: Ninput(2))
ui.pushButton_8.clicked.connect(lambda: Ninput(6))
ui.pushButton_9.clicked.connect(lambda: Ninput(3))
ui.pushButton_10.clicked.connect(lambda: Ninput(0))
ui.pushButton_11.clicked.connect(lambda: Ninput("."))
ui.pushButton_12.clicked.connect(lambda: ui.label_10.setText(str(Equals(ui.label_11.text()))))
ui.pushButton_12.clicked.connect(ui.label_11.clear)
ui.pushButton_13.clicked.connect(lambda: Ninput(" * " ))
ui.pushButton_14.clicked.connect(lambda: Ninput(" / "))
ui.pushButton_15.clicked.connect(lambda: Ninput(" - "))
ui.pushButton_16.clicked.connect(lambda: Ninput(" + "))
ui.pushButton_17.clicked.connect(ui.label_11.clear)
ui.pushButton_17.clicked.connect(ui.label_10.clear)
ui.pushButton_18.clicked.connect(lambda: Delete())
ui.pushButton_19.clicked.connect(lambda: Ninput(str(round(math.pi, 5))))
ui.pushButton_20.clicked.connect(lambda: ui.label_10.setText(str(math.log2(int(ui.label_11.text())))))
ui.pushButton_20.clicked.connect(ui.label_11.clear)
ui.pushButton_21.clicked.connect(lambda: ui.label_10.setText(str(Complex(ui.lineEdit_2.text(),ui.lineEdit_3.text(),
                                                                         ui.lineEdit_5.text(),ui.lineEdit_4.text(),
                                                                         ui.comboBox.currentIndex()))))



sys.exit(app.exec_())