import rcres
from PyQt5 import QtCore, QtGui, QtWidgets
from reg import rgr


class Ui_Register(object):
    def loginwin(self):
        from main import Ui_Login
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupL(self.window)
        self.window.show()

    def checklines(self):
        if(self.FName.text() == "" or self.LName.text() == "" or self.Username.text() == "" or self.Email.text() == "" or self.PWord.text() == "" or self.RPword.text() == ""):
            self.PWCheck.setText("Fill out all of the information!")
        else:
            a = self.reg1.checkUser(self.Username.text())
            if(a == "Exist"):
                self.PWCheck.setText("Username Exist")
            elif(a == "DoesNotExist"):
                if (len(self.PWord.text()) > 6):
                    if (self.PWord.text() != self.RPword.text()):
                        self.PWCheck.setText("Password do not match")
                    else:
                        self.reg1.setPassword(self.PWord.text())
                        self.reg1.setFirstName(self.FName.text())
                        self.reg1.setLastName(self.LName.text())
                        self.reg1.setEmail(self.Email.text())
                        self.reg1.sendToFile()
                        self.loginwin()
                        self.Register.close()

                else:
                    self.PWCheck.setText(
                        "Password should be greater than 6 characters")

    def setupR(self, Register):
        self.reg1 = rgr()
        self.Register = Register
        Register.setWindowIcon(QtGui.QIcon(':/images/logo.png'))
        Register.setObjectName("Register")
        Register.resize(540, 360)
        Register.setMinimumSize(QtCore.QSize(370, 360))
        Register.setMaximumSize(QtCore.QSize(370, 360))
        Register.setStyleSheet("*{\n"
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
        self.toolButton = QtWidgets.QToolButton(Register)

        self.frame = QtWidgets.QFrame(Register)
        self.frame.setGeometry(QtCore.QRect(20, 10, 331, 341))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 5, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.signup = QtWidgets.QPushButton(self.frame)
        self.signup.setGeometry(QtCore.QRect(40, 290, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.signup.setFont(font)
        self.signup.setObjectName("signup")
        self.PWord = QtWidgets.QLineEdit(self.frame)
        self.PWord.setGeometry(QtCore.QRect(40, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.PWord.setFont(font)
        self.PWord.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PWord.setObjectName("PWord")
        self.cancel = QtWidgets.QPushButton(self.frame)
        self.cancel.setGeometry(QtCore.QRect(170, 290, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.FName = QtWidgets.QLineEdit(self.frame)
        self.FName.setGeometry(QtCore.QRect(40, 50, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.FName.setFont(font)
        self.FName.setObjectName("FName")
        self.LName = QtWidgets.QLineEdit(self.frame)
        self.LName.setGeometry(QtCore.QRect(40, 95, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.LName.setFont(font)
        self.LName.setObjectName("LName")
        self.RPword = QtWidgets.QLineEdit(self.frame)
        self.RPword.setGeometry(QtCore.QRect(170, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.RPword.setFont(font)
        self.RPword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.RPword.setObjectName("RPword")
        self.PWCheck = QtWidgets.QLabel(self.frame)
        self.PWCheck.setGeometry(QtCore.QRect(60, 270, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(6)
        self.PWCheck.setFont(font)
        self.PWCheck.setStyleSheet("QLabel{\n"
                                   "color: black;\n"
                                   "font-size: 10;\n"
                                   "}")
        self.PWCheck.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.PWCheck.setFrameShadow(QtWidgets.QFrame.Plain)
        self.PWCheck.setText("")
        self.PWCheck.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.PWCheck.setObjectName("PWCheck")
        self.RegCheck = QtWidgets.QLabel(self.frame)
        self.RegCheck.setGeometry(QtCore.QRect(40, 50, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.RegCheck.setFont(font)
        self.RegCheck.setStyleSheet("")
        self.RegCheck.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.RegCheck.setFrameShadow(QtWidgets.QFrame.Plain)
        self.RegCheck.setText("")
        self.RegCheck.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.RegCheck.setObjectName("RegCheck")
        self.toolButton_2 = QtWidgets.QToolButton(Register)
        self.toolButton_2.setGeometry(QtCore.QRect(360, 100, 181, 151))
        self.Username = QtWidgets.QLineEdit(Register)
        self.Username.setGeometry(QtCore.QRect(60, 150, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.Email = QtWidgets.QLineEdit(Register)
        self.Email.setGeometry(QtCore.QRect(60, 200, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.Email.setFont(font)
        self.Email.setObjectName("Email")

        self.retranslateUi(Register)
        self.signup.clicked.connect(self.checklines)
        self.cancel.clicked.connect(self.loginwin)
        self.cancel.clicked.connect(Register.close)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Register"))
        self.label.setText(_translate("Register", "Create Account"))
        self.signup.setText(_translate("Register", "Sign Up"))
        self.PWord.setPlaceholderText(_translate("Register", " Password"))
        self.cancel.setText(_translate("Register", "Cancel"))
        self.FName.setPlaceholderText(_translate("Register", " First Name"))
        self.LName.setPlaceholderText(_translate("Register", " Last Name"))
        self.RPword.setPlaceholderText(
            _translate("Register", " Re-Enter Password"))
        self.toolButton_2.setText(_translate("Register", "..."))
        self.Username.setPlaceholderText(_translate("Register", " Username"))
        self.Email.setPlaceholderText(_translate("Register", " Email Address"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QDialog()
    ui = Ui_Register()
    ui.setupR(Register)
    Register.show()
    sys.exit(app.exec_())
