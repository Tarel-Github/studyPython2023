# 윈도우 창닫기 앱
# 2023.02.09
# SMS
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 버튼 정의
        btn = QPushButton('Quit', self)
        # 버튼 위치
        btn.move(320,170)
        btn.resize(btn.sizeHint())
        # 버튼 툴팁
        btn.setToolTip('<b>경고</b>누르는 순간 즉시 종료')
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowIcon(QIcon('./Day09/iot.png'))
        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 400, 200) # x, y 좌표와 넓이와 높이
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
