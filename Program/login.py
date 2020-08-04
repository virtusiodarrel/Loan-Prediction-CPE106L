import rcres
from PyQt5 import QtCore, QtGui, QtWidgets
from log import lgn


class Ui_Login(object):
    def regwin(self):
        from register import Ui_Register
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Register()
        self.ui.setupR(self.window)
        self.window.show()

    def menu(self):
        from menu import Ui_Menu
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Menu()
        self.ui.setupM(self.window)
        self.window.show()

    def log(self):
        a = self.log1.checkAccount(
            self.userfield1.text(), self.passfield1.text())
        if(a == "correct"):
            self.Login.close()
            self.menu()
        elif(a == "incorrect"):
            self.statuscheck.setText("Password is incorrect")
        else:
            self.statuscheck.setText("User does not exist")

    def _addShadowEffect(self, item):
        effect = QtWidgets.QGraphicsDropShadowEffect()
        effect.setBlurRadius(3)
        effect.setColor(QtGui.QColor("black"))
        effect.setOffset(0.5, 0.5)
        item.setGraphicsEffect(effect)

    def setupL(self, Login):
        self.log1 = lgn()
        self.Login = Login
        Login.setWindowIcon(QtGui.QIcon('logo.png'))
        Login.setObjectName("Login")
        Login.resize(540, 360)
        Login.setMinimumSize(QtCore.QSize(540, 360))
        Login.setMaximumSize(QtCore.QSize(540, 360))
        Login.setStyleSheet("*{\n"
                            "font-family: Verdana;\n"
                            "}\n"
                            "QDialog{\n"
                            "border-image:url(:/images/bg1.png)\n"
                            "}\n"
                            "QToolButton{\n"
                            "background: transparent\n"
                            "}\n"
                            "QPushButton{\n"
                            "color:#dfdfdf;\n"
                            "background:#009060;\n"
                            "border-radius:10px\n"
                            "}\n"
                            "QFrame{\n"
                            "background:rgba(50, 100, 42, 0.94);\n"
                            "border-radius: 10px;\n"
                            "}\n"
                            "QLabel{\n"
                            "color:#dfdfdf;\n"
                            "background: transparent;\n"
                            "}\n"
                            "QLineEdit{\n"
                            "border-radius:10px;\n"
                            "background: #dfdfdf;\n"
                            "}\n"
                            "QPushButton:Hover{\n"
                            "color:black;\n"
                            "background:#dfdfdf;\n"
                            "border-radius:10px\n"
                            "}")

        self.frame = QtWidgets.QFrame(Login)
        self.frame.setGeometry(QtCore.QRect(30, 20, 271, 320))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily(" Verdana")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(35, 40, 200, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.loginbutton1 = QtWidgets.QPushButton(self.frame)
        self.loginbutton1.setGeometry(QtCore.QRect(20, 220, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.loginbutton1.setFont(font)
        self.loginbutton1.setObjectName("loginbutton1")
        self.userfield1 = QtWidgets.QLineEdit(self.frame)
        self.userfield1.setGeometry(QtCore.QRect(30, 110, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.userfield1.setFont(font)
        self.userfield1.setObjectName("userfield1")
        self.passfield1 = QtWidgets.QLineEdit(self.frame)
        self.passfield1.setGeometry(QtCore.QRect(30, 170, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.passfield1.setFont(font)
        self.passfield1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passfield1.setObjectName("passfield1")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(-30, 70, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(-30, 130, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.statuscheck = QtWidgets.QLabel(self.frame)
        self.statuscheck.setGeometry(QtCore.QRect(30, 260, 211, 75))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.statuscheck.setFont(font)
        self.statuscheck.setText("")
        self.statuscheck.setAlignment(QtCore.Qt.AlignCenter)
        self.statuscheck.setObjectName("statuscheck")
        self.toolButton_2 = QtWidgets.QToolButton(Login)
        self.toolButton_2.setGeometry(QtCore.QRect(300, 70, 241, 201))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/logo.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(900, 900))
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_5 = QtWidgets.QLabel(Login)
        self.label_5.setGeometry(QtCore.QRect(345, 300, 150, 21))
        self._addShadowEffect(self.label_5)
        font = QtGui.QFont()
        font.StyleStrategy()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.regbutton = QtWidgets.QPushButton(Login)
        self.regbutton.setGeometry(QtCore.QRect(375, 320, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.regbutton.setFont(font)
        self.regbutton.setObjectName("regbutton")

        self.retranslateUi(Login)
        self.loginbutton1.clicked.connect(self.log)
        self.regbutton.clicked.connect(self.regwin)
        self.regbutton.clicked.connect(Login.close)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "Loan Prediction"))
        self.label_2.setText(_translate(
            "Login", "Please log in to your account"))
        self.loginbutton1.setText(_translate("Login", "LOGIN"))
        self.userfield1.setPlaceholderText(
            _translate("Login", " Username"))
        self.passfield1.setPlaceholderText(_translate("Login", " *****"))
        self.label_3.setText(_translate("Login", "Username :"))
        self.label_4.setText(_translate("Login", "Password :"))
        self.toolButton_2.setText(_translate("Login", "..."))
        self.label_5.setText(_translate("Login", "Don\'t have an account?"))
        self.regbutton.setText(_translate("Login", "Sign-up here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupL(Login)
    Login.show()
    sys.exit(app.exec_())
