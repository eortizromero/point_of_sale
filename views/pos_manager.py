# coding: latin1

from PyQt4.QtGui import QMainWindow, \
    QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, \
    QCheckBox, QCursor
from PyQt4.QtCore import Qt, QPropertyAnimation, QRect
import re
import xmlrpclib


class PosManager(QMainWindow):
    def __init__(self, parent=None):
        super(PosManager, self).__init__(parent)
        self.width, self.height = 800, 450
        self.crear_interfaz(self.width, self.height)
        self.setWindowTitle('Odoo Point Of Sale | Database Manager')
        self.logged = False
        self.common = '/xmlrpc/common'
        self.object = '/xmlrpc/object'
        self.db = '/xmlrpc/db'

    def crear_interfaz(self, width, height):
        self.setMinimumSize(width, height)
        self.setObjectName('pos_manager_form_window')
        self.setMaximumSize(width, height)
        height_server = 250
        width_server = 400
        width_widgets = (width / 2) - (width_server / 2)
        pos_x = (width / 3)
        width_small = width_server / 3

        self.container_connect = QWidget(self)
        self.container_connect.setMinimumSize(width, height)
        self.container_connect.setMaximumSize(width, height)
        self.container_connect.setObjectName('pos_manager_container_connect')

        self.title = QLabel(self.container_connect)
        self.title.setText("P O I N T  O F  S A L E")
        self.title.setGeometry(0, 50, width, 20)
        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.title.setObjectName('pos_manager_title')

        self.description = QLabel(self.container_connect)
        self.description.setText("Para conectar con el Punto de Venta, \nIngresa la dirección del Servidor:")
        self.description.setGeometry(0, 130, width, 60)
        self.description.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.description.setObjectName('pos_manager_description')

        self._error = QLabel(self.container_connect)
        self._error.setText("")
        self._error.setGeometry(205, 190, width_server, 50)
        self._error.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self._error.setObjectName('pos_error_msg')
        self._error.setVisible(False)

        self.protocol = QLineEdit(self.container_connect)
        self.protocol.setPlaceholderText('Protocolo')
        self.protocol.setText("http")
        self.protocol.setGeometry(165, height_server, width_small, 40)
        self.protocol.setObjectName('pos_protocol')
        self.protocol.setAcceptDrops(False)

        self.host = QLineEdit(self.container_connect)
        self.host.setPlaceholderText('Servidor')
        self.host.setGeometry(pos_x, height_server, width_server - 100, 40)
        self.host.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.host.setObjectName('pos_host')
        self.host.setAcceptDrops(False)

        self.port = QLineEdit(self.container_connect)
        self.port.setPlaceholderText('Puerto')
        self.port.setText('8069')
        self.port.setGeometry(pos_x + width_server - 140, height_server, width_small, 40)
        self.port.setObjectName('pos_port')
        self.port.setAcceptDrops(False)

        self.checkbox_rememberme = QCheckBox(self.container_connect)
        self.checkbox_rememberme.setLayoutDirection(Qt.RightToLeft)
        self.checkbox_rememberme.setGeometry(pos_x - 100, height_server + 60, 40, 20)
        self.checkbox_rememberme.setObjectName("login_rememberme")
        self.checkbox_rememberme.setCursor(QCursor(Qt.PointingHandCursor))

        self.label_icon = QLabel(self.checkbox_rememberme)
        self.label_icon.setGeometry(0, 0, 20, 20)
        self.label_icon.setObjectName("label_icon")

        self.label_rememberme = QLabel(self.container_connect)
        self.label_rememberme.setText("RECUÉRDAME ESTE SERVIDOR")
        self.label_rememberme.setGeometry(210, height_server + 60, 265, 20)
        self.label_rememberme.setObjectName("label_rememberme")

        self.button_connect = QPushButton(self.container_connect)
        self.button_connect.setText("CONECTAR")
        self.button_connect.setGeometry(width_widgets + (width_widgets/2), height_server + 90, width_server - 200, 40)
        self.button_connect.setObjectName("pos_button_connect")

        self.container_database = QWidget(self)
        self.container_database.setMinimumSize(width, height)
        self.container_database.setMaximumSize(width, height)
        self.container_database.setObjectName('pos_manager_container_database')
        self.container_database.setVisible(False)

        self.title_database = QLabel(self.container_database)
        self.title_database.setText("Selecciona tu Base de Datos")
        self.title_database.setGeometry(0, 50, width, 20)
        self.title_database.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.title_database.setObjectName('pos_title_database')

        self.listWidget = QListWidget(self.container_database)
        self.listWidget.setGeometry(width_widgets, 90, width_server, 150)
        self.listWidget.setObjectName('pos_list_db')

        # Login Form

        self.container_login = QWidget(self)
        self.container_login.setMinimumSize(width, height)
        self.container_login.setMaximumSize(width, height)
        self.container_login.setObjectName('pos_manager_container_login')
        self.container_login.setVisible(False)

        self.title = QLabel(self.container_login)
        self.title.setText('INICIA SESIÓN')
        self.title.setGeometry(0, 30, width, 40)
        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.title.setObjectName('pos_title_login')

        self.database_select = QLineEdit(self.container_login)
        self.database_select.setPlaceholderText('Base de Datos')
        self.database_select.setGeometry(pos_x, 80, width_server - 100, 40)
        self.database_select.setObjectName('login_database_select')
        self.database_select.setEnabled(False)
        self.database_select.setAcceptDrops(False)

        self.button_change_db = QPushButton(self.container_login)
        self.button_change_db.setGeometry(pos_x + 190, 80, 110, 40)
        self.button_change_db.setText("Selecciona")
        self.button_change_db.setObjectName("button_change_db")
        self.button_change_db.setCursor(QCursor(Qt.PointingHandCursor))

        self.username = QLineEdit(self.container_login)
        self.username.setPlaceholderText('Nombre de usuario')
        self.username.setGeometry(pos_x, 140, width_server - 100, 40)
        self.username.setObjectName('login_username')
        self.username.setAcceptDrops(False)

        self.password = QLineEdit(self.container_login)
        self.password.setPlaceholderText('Contraseña')
        self.password.setGeometry(pos_x, 200, width_server - 100, 40)
        self.password.setObjectName('login_password')
        self.password.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton(self.container_login)
        self.button_login.setGeometry(pos_x + 50, 260, width_server - 200, 40)
        self.button_login.setText("INICIAR SESIÓN")
        self.button_login.setObjectName("button_login")

        self.button_connect.clicked.connect(self._valid_empty_field)
        self.checkbox_rememberme.clicked.connect(self.remember_me)
        self.button_login.clicked.connect(self._login)

    def _valid_empty_field(self):
        protocol = self.protocol.text()
        host = self.host.text()
        port = self.port.text()

        if protocol == '':
            self.protocol.setFocus(True)
            self._error.setVisible(True)
            self._error.setText("Falta el protocolo")
        elif host == '':
            self.host.setFocus(True)
            self._error.setVisible(True)
            self._error.setText("Falta el servidor")
        elif port == '':
            self._error.setVisible(True)
            self.port.setFocus(True)
            self._error.setText("Falta el puerto")
        else:
            self._error.setVisible(False)
            self.server_name = self.format_server(protocol,host, port)
            if self.regex_server(self.server_name):
                self._connect_server_xmlrpc(self.server_name)
            else:
                self._error.setVisible(True)
                self._error.setText(self.server_name + "\n No coincide con un servidor, intente ingresar el formato correcto.")

    def _connect_server_xmlrpc(self, server_name):
        url_db = self.db
        try:
            connect = xmlrpclib.ServerProxy(server_name + '{}'.format(url_db))
            list_db = connect.list()
            self.container_connect.setVisible(False)
            self.container_database.setVisible(True)

            for i in list_db:
                item = QListWidgetItem(i)
                self.listWidget.addItem(item)
            self.listWidget.currentItemChanged.connect(self._database_selected)

        except Exception as ex:
            self._error.setVisible(True)
            self._error.setText('{:s}'.format(ex))

    def _load_login_form(self):
        self.container_database.setVisible(False)
        self.container_login.setVisible(True)

    def _database_selected(self):
        self._load_login_form()
        db = self.listWidget.currentItem().text()
        self.database_select.setText(db)

    def _login(self):
        url_common = self.common
        server_name = self.server_name
        self._database = str(self.database_select.text())
        self._username = str(self.username.text())
        self._password = str(self.password.text())

        session = xmlrpclib.ServerProxy(server_name+url_common)
        uid = session.login(self._database, self._username, self._password)

        if uid != 0:
            self.logged = True
            PosManager.hide(self)
            from pos_application import PosApplication
            self.app = PosApplication()
            self.app.show()
            with open("static/src/css/style.css", "r") as t:
                tema = t.read()
            self.app.setStyleSheet(tema)
            print 'Usuario logueado ' + str(uid)

    def format_server(self, protocol, host, port):
        format_server = ('{}://{}:{}'.format(protocol, host, port))
        return format_server

    def regex_server(self, server):
        # Regex for Odoo Address Server added by user
        # Return False if not is a valid address
        regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if regex.search(server):
            return True

    def anim_left(self):
        animation = QPropertyAnimation(self.label_icon, "geometry")
        animation.setDuration(250)
        animation.setStartValue(QRect(0, 0, 20, 20))
        animation.setEndValue(QRect(20, 0, 20, 20))
        animation.start()
        self.animation = animation

    def anim_right(self):
        animation = QPropertyAnimation(self.label_icon, "geometry")
        animation.setDuration(250)
        animation.setStartValue(QRect(20, 0, 20, 20))
        animation.setEndValue(QRect(0, 0, 20, 20))
        animation.start()
        self.animation = animation

    def remember_me(self):
        if self.checkbox_rememberme.isChecked():
            self.anim_left()
            self.label_icon.setGeometry(20, 0, 20, 20)
        else:
            self.anim_right()
            self.label_icon.setGeometry(0, 0, 20, 20)
