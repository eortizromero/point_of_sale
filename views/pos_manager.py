# coding: latin1

from PyQt4.QtGui import QMainWindow, \
    QWidget, QLabel, QLineEdit
from PyQt4.QtCore import Qt


class PosManager(QMainWindow):
    def __init__(self, parent=None):
        super(PosManager, self).__init__(parent)
        self.width, self.height = 800, 650
        self.crear_interfaz(self.width, self.height)
        self.setWindowTitle('Odoo Point Of Sale | Database Manager')

    def crear_interfaz(self, width, height):
        self.setMinimumSize(width, height)
        self.setObjectName('pos_manager_form_window')
        self.setMaximumSize(width, height)

        self.container = QWidget(self)
        self.container.setMinimumSize(width, height)
        self.container.setMaximumSize(width, height)
        self.container.setObjectName('pos_manager_container')

        self.title = QLabel(self.container)
        self.title.setText("P O I N T  O F  S A L E")
        self.title.setGeometry(0, 50, width, 20)
        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.title.setObjectName('pos_manager_title')

        self.description = QLabel(self.container)
        self.description.setText("Para conectar con el Punto de Venta, \nIngresa la dirección del Servidor:")
        self.description.setGeometry(0, 120, width, 60)
        self.description.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.description.setObjectName('pos_manager_description')

        width_server = 300
        self.server_name = QLineEdit(self.container)
        self.server_name.setPlaceholderText('S E R V I D O R')
        self.server_name.setGeometry((width/2) - (width_server / 2), 200, width_server, 40)
        self.server_name.setObjectName('pos_server_name')
        self.server_name.setAcceptDrops(False)



