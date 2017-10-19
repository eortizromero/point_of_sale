# coding:latin-1

from PyQt4.QtGui import QMainWindow, QWidget

class PosApplication(QMainWindow):
    def __init__(self):
        super(PosApplication, self).__init__()
        self.setWindowTitle('Point Of Sale')
        self.setMinimumSize(1024, 600)
        self.setObjectName('pos_application_window')
        self.setupUi()


    def setupUi(self):
        self.pos_container = QWidget(self)



