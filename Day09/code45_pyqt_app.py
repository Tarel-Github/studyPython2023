import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(400, 200)
        self.show()#핵심!



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


