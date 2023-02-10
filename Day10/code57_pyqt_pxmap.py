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
        # 이미지 사이즈 강제 변경 .scaledToWidth(w)
        pixmap = QPixmap('./Day10/cat.png').scaledToWidth(800)

        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)
        lblSize = QLabel(str(pixmap.width()) + 'x' + str(pixmap.height()))
        lblSize.setAlignment(Qt.AlignmentFlag.AlignCenter) # Qt.AlignCenter 가능

        vbox = QVBoxLayout(self)
        vbox.addWidget(lblImage)
        vbox.addWidget(lblSize)

        self.setLayout(vbox)

        # 필수설정
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        self.setWindowTitle('이미지 위젯')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
