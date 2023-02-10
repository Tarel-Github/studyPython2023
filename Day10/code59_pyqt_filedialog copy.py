# 라인에디트 - textbox
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        
        openFile = QAction(QIcon('open.png'), '&Open', self)#아이콘이 없어서 안뜸
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('파일 열기')



        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        #필수 설정
        self.setWindowTitle('라인에디트')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
