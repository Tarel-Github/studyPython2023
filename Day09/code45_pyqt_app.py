# 기본 탬플릿
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple Window') # 창의 타이틀 이름을 바꿈
        #self.move(800, 200) # 처음 창의 위치를 선정, 0,0은 왼쪽 위, 기본값은 정 중앙
        self.resize(400, 200) # 창의 크기를 바꿈
        self.show()#핵심! 창을 출력



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


