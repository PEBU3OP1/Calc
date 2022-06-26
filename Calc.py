from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from calc_intrface import Ui_Dialog

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
    ui.lineEdit.setText(ui.lineEdit.text() + pb_n)

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
ui.pushButton_13.clicked.connect(lambda: Ninput("*"))
ui.pushButton_14.clicked.connect(lambda: Ninput("/"))
ui.pushButton_15.clicked.connect(lambda: Ninput("-"))
ui.pushButton_16.clicked.connect(lambda: Ninput("+"))
ui.pushButton_17.clicked.connect(lambda: Ninput("i"))
ui.pushButton_19.clicked.connect(lambda: Ninput("("))
ui.pushButton_20.clicked.connect(lambda: Ninput(")"))




sys.exit(app.exec_())