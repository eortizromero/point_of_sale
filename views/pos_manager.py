# coding: latin1

from PyQt4.QtGui import QMainWindow, \
    QWidget, QLabel, QLineEdit, QPushButton
from PyQt4.QtCore import Qt
import re

class PosManager(QMainWindow):
    def __init__(self, parent=None):
        super(PosManager, self).__init__(parent)
        self.width, self.height = 800, 450
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
        width_widgets = (width/2) - (width_server / 2) 
        self.server_name = QLineEdit(self.container)
        self.server_name.setPlaceholderText('SERVIDOR')
        self.server_name.setGeometry(width_widgets, 200, width_server, 40)
        self.server_name.setObjectName('pos_server_name')
        self.server_name.setAcceptDrops(False)

        self.button_connect = QPushButton(self.container)
        self.button_connect.setText("CONECTAR")
        self.button_connect.setGeometry(width_widgets, 260, width_server, 40)
        self.button_connect.setObjectName("pos_button_connect")

        self.button_connect.clicked.connect(self._valid_empty_field)

    def _valid_empty_field(self):
        server_name = self.server_name.text()
        
        if server_name == '':
            self.server_name.setFocus(True)
        else:
            if self.regex_server(server_name):
                print "Validando server"
            else:
                print "no coincide con ningun servidor..."

    def regex_server(self, server):
        # Regex for Odoo Address Server added by user
        # Return False if not is a valid address
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if regex.search(server):
            return True
