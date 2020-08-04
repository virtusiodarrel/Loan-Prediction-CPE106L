import sklearn
import numpy as np
import pandas as pd
import sys
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from math import sqrt
import rcres
from PyQt5 import QtCore, QtGui, QtWidgets

# ignore all future warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore')

# import math modules
# import required libraries
# import necessary modules
# import libraries
# import keras modules


class Ui_Menu(object):
    def openFile(self):
        _translate = QtCore.QCoreApplication.translate
        options = QFileDialog.Options()
        fileName = QFileDialog.getOpenFileName(
            None, "Open File", "", "All Files (*);;Python Files (*.py)", options=options)
        path = fileName[0]
        self.lineEdit.setText(_translate("Menu", path))

    def openFile1(self):
        _translate = QtCore.QCoreApplication.translate
        options = QFileDialog.Options()
        fileName = QFileDialog.getOpenFileName(
            None, "Open File", "", "All Files (*);;Python Files (*.py)", options=options)
        path = fileName[0]
        self.lineEdit1.setText(_translate("Menu", path))

    def loanP1(self):
        train = pd.read_csv("train_data.csv")
        test = pd.read_csv("test_data.csv")

        # make a copy of original data
        # so that even if we have to make any changes in these datasets we would not lose the original datasets
        #train_original = train.copy()
        #test_original = test.copy()

        # show the shape of the dataset i.e. no of rows, no of columns
        train.shape, test.shape

        # calculate train-test-split ratio
        train.shape[0]/(train.shape[0]+test.shape[0]
                        ), test.shape[0]/(train.shape[0]+test.shape[0])

        # check for missing values
        train.isnull().sum()

        # replace missing values with the mode
        train['Gender'].fillna(train['Gender'].mode()[0], inplace=True)
        train['Married'].fillna(train['Married'].mode()[0], inplace=True)
        train['Dependents'].fillna(train['Dependents'].mode()[0], inplace=True)
        train['Self_Employed'].fillna(
            train['Self_Employed'].mode()[0], inplace=True)
        train['Credit_History'].fillna(
            train['Credit_History'].mode()[0], inplace=True)

        train['Loan_Amount_Term'].value_counts()

        # replace missing value with the mode
        train['Loan_Amount_Term'].fillna(
            train['Loan_Amount_Term'].mode()[0], inplace=True)

        # replace missing values with the median value due to outliers
        train['LoanAmount'].fillna(train['LoanAmount'].median(), inplace=True)

        # check whether all the missing values are filled in the Train dataset
        train.isnull().sum()

        # replace missing values in Test set with mode/median from Training set
        test['Gender'].fillna(train['Gender'].mode()[0], inplace=True)
        test['Dependents'].fillna(train['Dependents'].mode()[0], inplace=True)
        test['Self_Employed'].fillna(
            train['Self_Employed'].mode()[0], inplace=True)
        test['Credit_History'].fillna(
            train['Credit_History'].mode()[0], inplace=True)
        test['Loan_Amount_Term'].fillna(
            train['Loan_Amount_Term'].mode()[0], inplace=True)
        test['LoanAmount'].fillna(train['LoanAmount'].median(), inplace=True)

        # check whether all the missing values are filled in the Test dataset
        test.isnull().sum()

        # Outliner Treatment
        # Removing skewness in LoanAmount variable by log transformation
        train['LoanAmount_log'] = np.log(train['LoanAmount'])
        test['LoanAmount_log'] = np.log(test['LoanAmount'])

        # drop Loan_ID
        train = train.drop('Loan_ID', axis=1)
        test = test.drop('Loan_ID', axis=1)

        # drop "Loan_Status" and assign it to target variable
        X = train.drop('Loan_Status', 1)
        y = train.Loan_Status

        # adding dummies to the dataset
        X = pd.get_dummies(X)
        train = pd.get_dummies(train)
        test = pd.get_dummies(test)

        X.shape, train.shape, test.shape

        X.head()
        # split the data into train and cross validation set
        x_train, x_cv, y_train, y_cv = train_test_split(
            X, y, test_size=0.3, random_state=0)
        # take a look at the dimension of the data
        x_train.shape, x_cv.shape, y_train.shape, y_cv.shape

        # fit the model
        model = LogisticRegression()
        model.fit(x_train, y_train)

        # make prediction
        pred_cv = model.predict(x_cv)

        # calculate accuracy score
        accuracy_score(y_cv, pred_cv)

        #########PREDICTION MODEL#######
        # prediction model
        cm = confusion_matrix(y_cv, pred_cv)

        sns.heatmap(cm, annot=True, fmt="d", cmap="Greens_r")
        plt.gcf().canvas.set_window_title('Loan Prediction')
        plt.title('Confusion Matrix')
        plt.xlabel('Predicted')
        plt.ylabel('True')

        plt.show()

    def classificationReport_clicked(self):
        from notif import Ui_Form
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

        train = pd.read_csv("train_data.csv")
        test = pd.read_csv("test_data.csv")

        # make a copy of original data
        # so that even if we have to make any changes in these datasets we would not lose the original datasets
        #train_original = train.copy()
        #test_original = test.copy()

        # show the shape of the dataset i.e. no of rows, no of columns
        train.shape, test.shape

        # calculate train-test-split ratio
        train.shape[0]/(train.shape[0]+test.shape[0]
                        ), test.shape[0]/(train.shape[0]+test.shape[0])

        # check for missing values
        train.isnull().sum()

        # replace missing values with the mode
        train['Gender'].fillna(train['Gender'].mode()[0], inplace=True)
        train['Married'].fillna(train['Married'].mode()[0], inplace=True)
        train['Dependents'].fillna(train['Dependents'].mode()[0], inplace=True)
        train['Self_Employed'].fillna(
            train['Self_Employed'].mode()[0], inplace=True)
        train['Credit_History'].fillna(
            train['Credit_History'].mode()[0], inplace=True)

        train['Loan_Amount_Term'].value_counts()

        # replace missing value with the mode
        train['Loan_Amount_Term'].fillna(
            train['Loan_Amount_Term'].mode()[0], inplace=True)

        # replace missing values with the median value due to outliers
        train['LoanAmount'].fillna(train['LoanAmount'].median(), inplace=True)

        # check whether all the missing values are filled in the Train dataset
        train.isnull().sum()

        # replace missing values in Test set with mode/median from Training set
        test['Gender'].fillna(train['Gender'].mode()[0], inplace=True)
        test['Dependents'].fillna(train['Dependents'].mode()[0], inplace=True)
        test['Self_Employed'].fillna(
            train['Self_Employed'].mode()[0], inplace=True)
        test['Credit_History'].fillna(
            train['Credit_History'].mode()[0], inplace=True)
        test['Loan_Amount_Term'].fillna(
            train['Loan_Amount_Term'].mode()[0], inplace=True)
        test['LoanAmount'].fillna(train['LoanAmount'].median(), inplace=True)

        # check whether all the missing values are filled in the Test dataset
        test.isnull().sum()

        # Outliner Treatment
        # Removing skewness in LoanAmount variable by log transformation
        train['LoanAmount_log'] = np.log(train['LoanAmount'])
        test['LoanAmount_log'] = np.log(test['LoanAmount'])

        # drop Loan_ID
        train = train.drop('Loan_ID', axis=1)
        test = test.drop('Loan_ID', axis=1)

        # drop "Loan_Status" and assign it to target variable
        X = train.drop('Loan_Status', 1)
        y = train.Loan_Status

        # adding dummies to the dataset
        X = pd.get_dummies(X)
        train = pd.get_dummies(train)
        test = pd.get_dummies(test)

        X.shape, train.shape, test.shape

        X.head()
        # split the data into train and cross validation set
        x_train, x_cv, y_train, y_cv = train_test_split(
            X, y, test_size=0.3, random_state=0)
        # take a look at the dimension of the data
        x_train.shape, x_cv.shape, y_train.shape, y_cv.shape

        # fit the model
        model = LogisticRegression()
        model.fit(x_train, y_train)

        # make prediction
        pred_cv = model.predict(x_cv)

        # calculate accuracy score
        accuracy_score(y_cv, pred_cv)

        #########PREDICTION MODEL#######
        # prediction model
        cm = confusion_matrix(y_cv, pred_cv)
        cm_to_list = cm.tolist()
        print(type(cm_to_list))

        with open("LoanStatus.txt", "w") as f:
            f.write("Loan Status\n\n")
            f.write(repr(cm_to_list))
            f.write("\n\n")
            f.write(str(cm_to_list[1][1]) +
                    " individuals are accepted to have loan\n")
            f.write(str(cm_to_list[0][0]) +
                    " individuals are not accepted to have loan\n")
            f.write(str(
                cm_to_list[0][1]) + " individuals are accepted to have loan but shouldn't be\n")
            f.write(str(
                cm_to_list[1][0]) + " individuals are not accepted to have loan but should be")

        f.close()

        print("__")

    def setupM(self, Menu):
        self.Menu = Menu
        Menu.setWindowIcon(QtGui.QIcon(':/images/logo.png'))
        Menu.setObjectName("Menu")
        Menu.resize(540, 360)
        Menu.setMinimumSize(QtCore.QSize(420, 365))
        Menu.setMaximumSize(QtCore.QSize(420, 365))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        Menu.setFont(font)
        Menu.setStyleSheet("*{\n"
                           "font-family: Verdana;\n"
                           "}\n"
                           "QDialog{\n"
                           "border-image: url(:/images/bg1.png)\n"
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
                           "QLineEdit{\n"
                           "border-radius:10px;\n"
                           "background: #dfdfdf;\n"
                           "}\n"
                           "QPushButton:Hover{\n"
                           "color:black;\n"
                           "background:#dfdfdf;\n"
                           "border-radius:10px\n"
                           "}")

        self.toolButton1 = QtWidgets.QToolButton(Menu)
        self.toolButton1.setGeometry(QtCore.QRect(130, 5, 150, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton1.setIcon(icon)
        self.toolButton1.setIconSize(QtCore.QSize(250, 250))
        self.toolButton1.setObjectName("toolButton1")

        self.lineEdit = QtWidgets.QLineEdit(Menu)
        self.lineEdit.setGeometry(QtCore.QRect(30, 160, 280, 25))
        self.lineEdit.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit1 = QtWidgets.QLineEdit(Menu)
        self.lineEdit1.setGeometry(QtCore.QRect(30, 200, 280, 25))
        self.lineEdit1.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setObjectName("lineEdit1")

        self.brws = QtWidgets.QPushButton(Menu)
        self.brws.setGeometry(QtCore.QRect(320, 160, 75, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.brws.setFont(font)
        self.brws.setObjectName("brws")

        self.brws1 = QtWidgets.QPushButton(Menu)
        self.brws1.setGeometry(QtCore.QRect(320, 200, 75, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.brws1.setFont(font)
        self.brws1.setObjectName("brws1")

        self.prdct = QtWidgets.QPushButton(Menu)
        self.prdct.setGeometry(QtCore.QRect(100, 235, 200, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.prdct.setFont(font)
        self.prdct.setObjectName("prdct")

        self.clssf = QtWidgets.QPushButton(Menu)
        self.clssf.setGeometry(QtCore.QRect(100, 295, 200, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.clssf.setFont(font)
        self.clssf.setObjectName("clssf")

        self.retranslateUi(Menu)
        self.brws.clicked.connect(self.openFile)
        self.brws1.clicked.connect(self.openFile1)
        self.clssf.clicked.connect(self.classificationReport_clicked)
        self.prdct.clicked.connect(self.loanP1)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Open"))
        self.lineEdit.setPlaceholderText(
            _translate("Menu", "  Open Test Data"))
        self.lineEdit1.setPlaceholderText(
            _translate("Menu", "  Open Train Data"))
        self.brws.setText(_translate("Menu", "Open File"))
        self.brws1.setText(_translate("Menu", "Open File"))
        self.prdct.setText(_translate("Menu", " Prediction Model"))
        self.clssf.setText(_translate("Menu", " Loan Status"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QDialog()
    ui = Ui_Menu()
    ui.setupM(Menu)
    Menu.show()
    sys.exit(app.exec_())
