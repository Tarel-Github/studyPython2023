# 라인에디트 - textbox
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.btnDlg = QPushButton('Dialog', self)
        self.btnDlg.move(100, 100)
        self.btnDlg.resize(100, 100)


        self.setLayout(vbox)    

        self.textEdit = QTextEdit(self)


        #필수 설정
        self.setWindowTitle('라인에디트')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
