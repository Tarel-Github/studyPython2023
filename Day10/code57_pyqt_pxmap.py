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
        self.btnDlg.move(30, 30)
        self.btnDlg.clicked.connect(self.onClicked)        
        
        self.txtInput = QLineEdit(self)
        self.txtInput.move(30, 60)


        #필수 설정
        self.setWindowTitle('이미지 위젯')
        #self.showFullScreen()# 풀스크린
        self.setGeometry(400,400,300,300)
        self.show()

    def onClicked(self):
        text, ok = QInputDialog.getText(self, '인풋 타이얼로그', '이름을 적으시오')

        if ok:
            self.txtInput.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
