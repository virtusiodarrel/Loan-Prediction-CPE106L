import rcres
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def menu(self):
        from menu import Ui_Menu
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Menu()
        self.ui.setupM(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(358, 180)
        Form.setMinimumSize(QtCore.QSize(358, 180))
        Form.setMaximumSize(QtCore.QSize(358, 180))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(105, 232, 165);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 130, 61, 31))
        self.pushButton.setStyleSheet("font: 8pt \"Verdana\";\n"
                                      "color:#dfdfdf;\n"
                                      "background:#009060;\n"
                                      "border-radius:10px\n"

                                      "}\n")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(75, 80, 281, 20))
        self.label.setStyleSheet("font: 12pt \"Verdana\";")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 10, 61, 61))
        self.pushButton_2.setStyleSheet("background-image: url(:/images/logo.png);\n"
                                        "border-image: url(:/images/logo.png);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Notification"))
        self.pushButton.setText(_translate("Form", "Exit"))
        self.label.setText(_translate(
            "Form", "LoanStatus.txt is created"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
