# coding: latin1

try:
    from PyQt4.QtGui import QApplication, QPalette, QLinearGradient, QColor, QBrush
except:
    print "No se encuentra la libreria PyQt4, instalela antes de iniciar la aplicación"

from views.pos_manager import PosManager

def run_app():
    import sys
    app = QApplication(sys.argv)
    db_manager = PosManager()
    db_manager.show()
    with open("static/src/css/style.css", "r") as t:
        tema = t.read()
    db_manager.setStyleSheet(tema)
    p = QPalette()
    gradient = QLinearGradient(0, 0, 0, 400)
    gradient.setColorAt(0.0, QColor(240, 240, 240))
    gradient.setColorAt(1.0, QColor(240, 160, 160))
    p.setBrush(QPalette.Window, QBrush(gradient))
    db_manager.setPalette(p)
    sys.exit(app.exec_())

if __name__ == '__main__':
    run_app()
