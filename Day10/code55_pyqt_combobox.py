# 체크박스 라디오 버튼
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lblOption = QLabel('선택값 : ', self)
        lblOption.move(20, 20)
        
        cbOption = QComboBox(self)
        cbOption.addItem('Option 1')
        cbOption.addItem('Option 2')
        cbOption.addItem('Option 3')
        cbOption.addItem('Option 4')
        cbOption.addItem('Option 5')
        cbOption.move(20, 40)
        cbOption.activated[str].connect(self.cbOption)        

        # 이 밑은 필수 설정
        self.setWindowTitle('콤보박스')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    # def onActiovation(elst)""

    def checkKorea(self, state):
        if state == Qt.CheckState.Checked:
            self.setWindowTitle('나는 한국인')
        else:
            self.setWindowTitle('뭐지?')

    def changeTitle(self, state):
        if state == Qt.CheckState.Checked: # Qt.Checked도 사용가능
            self.setWindowTitle('체크박스 체크')
        else:
            self.setWindowTitle('체크박스 체크해제')

if __name__== '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())