# 테스트용 자유롭게 편집하는 파일
import sys
from PyQt5.QtWidgets import QApplication, QAction , QMainWindow, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 상태바, 시간과 날짜
        now = QDate.currentDate()
        time = QTime.currentTime()
        self.statusBar().showMessage(now.toString('yyyy-MM-dd') + ' '+ time.toString('hh:mm:ss'))
        self.setWindowIcon(QIcon('./Day09/iot.png'))

        # 기본 코드
        self.setWindowTitle('Bar Window')
        self.move(50, 50)
        self.resize(400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
