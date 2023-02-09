import sys
from PyQt5.QtWidgets import *

class MyApp(QMainWindow):
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    