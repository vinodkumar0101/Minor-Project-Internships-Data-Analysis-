from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt
import sys
import pandas as pd

class CheckableComboBox(QComboBox):
    def __init__(self):
        super(CheckableComboBox, self).__init__()
        self.view().pressed.connect(self.handle_item_pressed)
        self.setModel(QStandardItemModel(self))
  
    # when any item get pressed
    def handle_item_pressed(self, index):
  
        # getting which item is pressed
        item = self.model().itemFromIndex(index)
  
        # make it check if unchecked and vice-versa
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)

    
    def uncheckall(self):
        for i in range(self.count()):
  
            # if item is checked add it to the list
            if self.item_checked(i):
                item = self.model().item(i, 0)
                item.setCheckState(Qt.Unchecked)
  
    # method called by check_items
    def item_checked(self, index):
  
        # getting item at index
        item = self.model().item(index, 0)
  
        # return true if checked else false
        return item.checkState() == Qt.Checked
  
    # calling method
    def check_items(self):
        # blank list
        checkedItems = []
  
        # traversing the items
        for i in range(self.count()):
  
            # if item is checked add it to the list
            if self.item_checked(i):
                checkedItems.append(i)
        return [self.model().item(index, 0).text() for index in checkedItems]
  
    # flush
    sys.stdout.flush()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 457)
        MainWindow.setMaximumSize(QtCore.QSize(470, 457))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 471, 431))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(210, 250, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formLayoutWidget = QtWidgets.QWidget(self.page)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 30, 351, 190))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        
        # self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        # self.lineEdit_7.setObjectName("lineEdit_7")
        # self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7) 
       
        self.comboBox2 = CheckableComboBox()
        self.comboBox2.setObjectName("comboBox2")
        df = pd.read_excel('C:/Users/prasanth/mini/output2.xlsx',nrows=100,usecols = "C")
        df['location']=list(df['location'].fillna("None").str.lower().str.split(","))
        locations= sorted(list(set(sum(df['location'].tolist(),[]))))
        for i in range(len(locations)):
            self.comboBox2.addItem(locations[i])
            item = self.comboBox2.model().item(i, 0)
            item.setCheckState(Qt.Unchecked)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox2)
       
        
        self.comboBox = CheckableComboBox()
        self.comboBox.setObjectName("comboBox")
        df = pd.read_excel('C:/Users/prasanth/mini/output2.xlsx',nrows=100,usecols = "L")
        df['Skills_required']=list(df['Skills_required'].fillna("None").str.lower().str.split(","))
        skills= sorted(list(set(sum(df['Skills_required'].tolist(),[]))))
        # traversing items
        for i in range(len(skills)):
            # adding item
            self.comboBox.addItem(skills[i])
            item = self.comboBox.model().item(i, 0)
  
            # setting item unchecked
            item.setCheckState(Qt.Unchecked)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(80, 290, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(30, 20, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Skills"))
        self.label_2.setText(_translate("MainWindow", "Stipend"))
        self.label_3.setText(_translate("MainWindow", "No of apllications"))
        self.label_4.setText(_translate("MainWindow", "Duration"))
        self.label_5.setText(_translate("MainWindow", "No of openings"))
        self.label_6.setText(_translate("MainWindow", "Candidates hired"))
        self.label_7.setText(_translate("MainWindow", "Location"))
        self.label_8.setText(_translate("MainWindow", "Your file is ready"))
        self.pushButton_2.setText(_translate("MainWindow", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
