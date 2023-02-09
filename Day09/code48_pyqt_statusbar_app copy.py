# 윈도우 창닫기 앱
# 2023.02.09
# SMS
import sys
from PyQt5.QtWidgets import QApplication, QAction , QMainWindow, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 액션
        # 액션에 아이콘을 추가
        actExit = QAction(QIcon('./Day09/exit.png'), 'Exit', self)
        # 액션에 단축키를 추가
        actExit.setShortcut('Ctrl+Q') # 단축키 지정
        # 액션에 설명을 추가
        actExit.setStatusTip('앱 종료')
        # 액션 작동시, 종료
        actExit.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)#네이티브 메뉴바를 쓰지 않겠다는 말
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 상태바
        self.statusBar().showMessage('StatusBar message')
        
        self.setWindowTitle('Bar Window') # 창의 타이틀 이름을 바꿈
        #self.move(800, 200) # 처음 창의 위치를 선정, 0,0은 왼쪽 위, 기본값은 정 중앙
        self.resize(400, 200) # 창의 크기를 바꿈
        self.show()#핵심! 창을 출력


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
