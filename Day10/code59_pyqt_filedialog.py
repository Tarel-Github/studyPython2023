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
        openFile.triggered.connect(self.onClicked)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        #필수 설정
        self.setWindowTitle('라인에디트')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def onClicked(self):
        fname = QFileDialog.getOpenFileName(self, '파일열기', './')

        if fname[0]:
            file = open(fname[0], 'rt', encoding='utf-8')
            with file:
                data = file.read()
                self.textEdit.setText(data)        
            file.close()

        QMessageBox.about(self, '성공', '로드했습니다.')

    def closeEvent(self, event) -> None:
        reply = QMessageBox.question(self, '종료', '저장하지 않은 정보가 날아갑니다.<br> 종료합니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept() # 프로그램 종료
        else:
            event.ignore() # 프로그램 계속
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
