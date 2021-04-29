import sys
from myapp3 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication)
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
import xml.dom.minidom 
import random          


class MyWin(QtWidgets.QMainWindow):
    text = []
    questions = []
    variants = []
    correct = []
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.textEdit.setFontPointSize(14)
        self.ui.textEdit_2.setFontPointSize(14)
        self.ui.textEdit_3.setFontPointSize(14)
        self.ui.textEdit_4.setFontPointSize(14)
        self.ui.textEdit_5.setFontPointSize(14)
        self.ui.textEdit_6.setFontPointSize(14)
        self.ui.textEdit_7.setFontPointSize(14)
        self.ui.textEdit_8.setFontPointSize(14)
        self.ui.textEdit_9.setFontPointSize(14)
        self.ui.textEdit_10.setFontPointSize(14)

        
        
        self.dom = xml.dom.minidom.parse('learn1.xml')
        self.collection = self.dom.documentElement
        self.linesArr = self.collection.getElementsByTagName("text")

        for line in self.linesArr:
            self.text.append(line.childNodes[0].data)
            self.questions.append(line.getAttribute('question'))
            self.variants.append(line.getAttribute('answers').split('**?**'))
            self.correct.append (line.getAttribute('correct'))

        random.shuffle(self.variants[0])
        random.shuffle(self.variants[1])
        random.shuffle(self.variants[2])
        random.shuffle(self.variants[3])
        random.shuffle(self.variants[4])
        random.shuffle(self.variants[5])
        random.shuffle(self.variants[6])
        random.shuffle(self.variants[7])
        random.shuffle(self.variants[8])
        random.shuffle(self.variants[9])
        
        self.ui.textEdit.setText(self.text[0])
        self.ui.textEdit_2.setText(self.text[1])
        self.ui.textEdit_3.setText(self.text[2])
        self.ui.textEdit_4.setText(self.text[3])
        self.ui.textEdit_5.setText(self.text[4])
        self.ui.textEdit_6.setText(self.text[5])
        self.ui.textEdit_7.setText(self.text[6])
        self.ui.textEdit_8.setText(self.text[7])
        self.ui.textEdit_9.setText(self.text[8])
        self.ui.textEdit_10.setText(self.text[9])


        self.ui.label.setText(self.questions[0])
        self.ui.label_2.setText(self.questions[1])
        self.ui.label_3.setText(self.questions[2])
        self.ui.label_4.setText(self.questions[3])
        self.ui.label_5.setText(self.questions[4])
        self.ui.label_6.setText(self.questions[5])
        self.ui.label_7.setText(self.questions[6])
        self.ui.label_8.setText(self.questions[7])
        self.ui.label_9.setText(self.questions[8])
        self.ui.label_10.setText(self.questions[9])


        self.ui.radioButton.  setText(self.variants[0][0])
        self.ui.radioButton_2.setText(self.variants[0][1])
        self.ui.radioButton_3.setText(self.variants[0][2])


        self.ui.radioButton_4.setText(self.variants[1][0])
        self.ui.radioButton_5.setText(self.variants[1][1])
        self.ui.radioButton_6.setText(self.variants[1][2])


        self.ui.radioButton_7.setText(self.variants[2][0])
        self.ui.radioButton_8.setText(self.variants[2][1])
        self.ui.radioButton_9.setText(self.variants[2][2])

        self.ui.radioButton_10.setText(self.variants[3][0])
        self.ui.radioButton_11.setText(self.variants[3][1])
        self.ui.radioButton_12.setText(self.variants[3][2])

        self.ui.radioButton_13.setText(self.variants[4][0])
        self.ui.radioButton_14.setText(self.variants[4][1])
        self.ui.radioButton_15.setText(self.variants[4][2])

        self.ui.radioButton_16.setText(self.variants[5][0])
        self.ui.radioButton_17.setText(self.variants[5][1])
        self.ui.radioButton_18.setText(self.variants[5][2])

        self.ui.radioButton_19.setText(self.variants[6][0])
        self.ui.radioButton_20.setText(self.variants[6][1])
        self.ui.radioButton_21.setText(self.variants[6][2])

        self.ui.radioButton_22.setText(self.variants[7][0])
        self.ui.radioButton_23.setText(self.variants[7][1])
        self.ui.radioButton_24.setText(self.variants[7][2])

        self.ui.radioButton_25.setText(self.variants[8][0])
        self.ui.radioButton_26.setText(self.variants[8][1])
        self.ui.radioButton_27.setText(self.variants[8][2])

        self.ui.radioButton_28.setText(self.variants[9][0])
        self.ui.radioButton_29.setText(self.variants[9][1])
        self.ui.radioButton_30.setText(self.variants[9][2])
        

        
        self.setWindowIcon(QIcon('helmet.png'))
        self.setWindowTitle("Informatics 2021/Application by Chernyshova Arina 2021")

        self.ui.tabWidget.setTabEnabled (1, False)
        self.ui.tabWidget.setTabEnabled (2, False)
        self.ui.tabWidget.setTabEnabled (3, False)
        self.ui.tabWidget.setTabEnabled (4, False)
        self.ui.tabWidget.setTabEnabled (5, False)
        self.ui.tabWidget.setTabEnabled (6, False)
        self.ui.tabWidget.setTabEnabled (7, False)
        self.ui.tabWidget.setTabEnabled (8, False)
        self.ui.tabWidget.setTabEnabled (9, False)
       
        self.ui.buttonGroup.   buttonClicked.connect(self.correctAnswer1)
        self.ui.buttonGroup_2. buttonClicked.connect(self.correctAnswer2)
        self.ui.buttonGroup_3. buttonClicked.connect(self.correctAnswer3)
        self.ui.buttonGroup_4. buttonClicked.connect(self.correctAnswer4)
        self.ui.buttonGroup_5. buttonClicked.connect(self.correctAnswer5)
        self.ui.buttonGroup_6. buttonClicked.connect(self.correctAnswer6)
        self.ui.buttonGroup_7. buttonClicked.connect(self.correctAnswer7)
        self.ui.buttonGroup_8. buttonClicked.connect(self.correctAnswer8)
        self.ui.buttonGroup_9. buttonClicked.connect(self.correctAnswer9)
        self.ui.buttonGroup_10.buttonClicked.connect(self.correctAnswer10)
        
    """  
    def initUI(self):
                
        self.setWindowIcon(QIcon('helmet.png'))
        self.setWindowTitle("Informatics 2021/Application by Chernyshova Arina 2021")
        self.show()
    """
    def correctAnswer1(self):
        for rb in self.ui.buttonGroup.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[0]:
                    self.ui.statusbar.showMessage("Correct! Task 2 is enabled now. ",5000)
                    self.ui.tab.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(1, True)
        
    def correctAnswer2(self):
        for rb in self.ui.buttonGroup_2.buttons():
            if rb. isChecked():
                if rb.text()==self.correct[1]:
                    self.ui.statusbar. showMessage("Correct! Task 3 is enabled now.", 5000)
                    self.ui.tab_2.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(2, True)
        
    def correctAnswer3(self):
        for rb in self.ui.buttonGroup_3.buttons():
            if rb. isChecked():
                if rb.text()==self.correct[2]:
                    self.ui.statusbar. showMessage("Correct! Task 4 is enabled now.", 5000)
                    self.ui.tab_3.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(3, True)
    def correctAnswer4(self):
        for rb in self.ui.buttonGroup_4.buttons():
            if rb. isChecked():
                if rb.text()==self.correct[3]:
                    self.ui.statusbar. showMessage("Correct! Task 5 is enabled now.", 5000)
                    self.ui.tab_4.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(4, True)
    def correctAnswer5(self):
        for rb in self.ui.buttonGroup_5.buttons():
            if rb. isChecked():
                if rb.text()==self.correct[4]:
                    self.ui.statusbar. showMessage("Correct! Task 6 is enabled now.", 5000)
                    self.ui.tab_5.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(5, True)
    def correctAnswer6(self):
        for rb in self.ui.buttonGroup_6.buttons():
            if rb. isChecked():
                if rb.text()==self.correct[5]:
                    self.ui.statusbar. showMessage("Correct! Task 7 is enabled now.", 5000)
                    self.ui.tab_6.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(6, True)
    def correctAnswer7(self):
        for rb in self.ui.buttonGroup_7.buttons():
            if rb. isChecked():
                if rb.text()==self.correct[6]:
                    self.ui.statusbar. showMessage("Correct! Task 8 is enabled now.", 5000)
                    self.ui.tab_7.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(7, True)
    def correctAnswer8(self):
        for rb in self.ui.buttonGroup_8.buttons():
            if rb. isChecked():
                if rb.text()==self.correct[7]:
                    self.ui.statusbar. showMessage("Correct! Task 9 is enabled now.", 5000)
                    self.ui.tab_8.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(8, True)
    def correctAnswer9(self):
       for rb in self.ui.buttonGroup_9.buttons():
            if rb. isChecked():
                if rb.text()==self.correct[8]:
                    self.ui.statusbar. showMessage("Correct! Task 10 is enabled now.", 5000) 
                    self.ui.tab_9.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(9, True)
    def correctAnswer10(self):
        for rb in self.ui.buttonGroup_10.buttons():
            if rb. isChecked():
                if rb.text()==self.correct[9]:
                    self.ui.statusbar. showMessage("Correct! It`s done", 5000)
                    self.ui.tab_10.setEnabled(False)
        
                       
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
