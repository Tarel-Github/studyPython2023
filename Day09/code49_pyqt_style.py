import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 스타일 설정
        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')
        lbl_red.setStyleSheet('color: red;'
                              'border-style: solid;'
                              'border-width: 5px;'
                              'border-color: #FA8072;'
                              'border-radius: 5px')

        lbl_green.setStyleSheet('color: green;'
                                'border-style: dashed;'
                                'border-width: 3px;'
                              'border-color: #7FFFD4;')
        lbl_blue.setStyleSheet('color: blue;'
                              'border-color: #87CEFA;'
                              'border-style: dashed;'
                              'border-width: 3px;'
                              'border-color: #1E90FF;')

        vbox = QVBoxLayout() # 세로로 구분짓는 레이아웃
        #vbox = QHBoxLayout() # 가로로 구분짓는 레이아웃
        vbox.addWidget(lbl_red) # 위젯 추가
        vbox.addWidget(lbl_green) # 위젯 추가
        vbox.addWidget(lbl_blue) # 위젯 추가

        self.setLayout(vbox) # 전체 레이아웃에 vbox를 추가

        self.setWindowTitle('스타일 지정')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
