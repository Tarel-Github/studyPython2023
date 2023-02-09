# 레이아웃 절대적 배치
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btnOk = QPushButton('OK')
        btnCancel = QPushButton('Cancel')
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)# 간격을 준것이다. 왼쪽에 1칸
        hbox.addWidget(btnOk)# OK버튼을 왼쪽에 붙여서 배치
        hbox.addWidget(btnCancel)
        hbox.addStretch(1)# 버튼 배치후, 오른쪽에 간격 1칸

        vbox = QVBoxLayout()
        vbox.addStretch(3)#간격을 준 것, 상단에 3칸
        vbox.addLayout(hbox)
        self.setLayout(vbox)# 이후 간격이 없으므로 버튼은 아래에 딱 붙음


        # 이 밑은 필수 설정
        self.setWindowTitle('박스 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__== '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())