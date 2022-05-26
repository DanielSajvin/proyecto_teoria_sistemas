from PyQt5.QtCore import QPropertyAnimation
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from PyQt5 import QtCore
import sqlite3
from inventory import Comunicacion


class MainView(QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        loadUi("views/proyectoTS.ui", self)
        self.show()

        self.btn_menu.clicked.connect(self.mover_menu)
        self.btn_inventario.hide()
        self.btn_registrar.hide()
        self.btn_actualizar.hide()
        self.btn_eliminar.hide()
        self.btn_inicio_de_sesion.show()
        self.btn_restaurar.hide()

        # ESTO ES LO QUE ESTUVE PROBANDO
        #self.data_base = Comunicacion()
        # -------------------
        #self.actualizar.clicked.connect(self.actualizar_producto)
        # AQUI TERMINA XD

        # Esta línea de codigo tiene que estar siempre a menos que...
        # self.btn_activar_opciones.hide()

        # ...Se Compruebe si es correcto el correo y contraseña y ponen este codigo
        self.btn_activar_opciones.show()

        # Botones que modifican la interfaz
        self.btn_minimizar.clicked.connect(self.minimizar)
        self.btn_restaurar.clicked.connect(self.normal)
        self.btn_maximizar.clicked.connect(self.maximizar)
        self.btn_cerrar.clicked.connect(lambda: self.close())

        # Botones para las paginas
        self.btn_activar_opciones.clicked.connect(self.activar_opciones)
        self.btn_inicio.clicked.connect(self.show_inicio)
        self.btn_inventario.clicked.connect(self.show_page_inventario)
        self.btn_registrar.clicked.connect(self.show_page_registar)
        self.btn_actualizar.clicked.connect(self.show_page_actualizar)
        self.btn_eliminar .clicked.connect(self.show_page_eliminar)
        self.btn_inicio_de_sesion.clicked.connect(self.show_page_iniciar_sesion)

    def show_inicio(self):
        self.stackedWidget.setCurrentWidget(self.page_inicio)

    def show_page_inventario(self):
        self.stackedWidget.setCurrentWidget(self.page_inventario)

    def show_page_registar(self):
        self.stackedWidget.setCurrentWidget(self.page_registrar)

    def show_page_actualizar(self):
        self.stackedWidget.setCurrentWidget(self.page_actualizar)

    def show_page_eliminar(self):
        self.stackedWidget.setCurrentWidget(self.page_eliminar)

    def show_page_iniciar_sesion(self):
        self.stackedWidget.setCurrentWidget(self.page_iniciar_sesion)

    def minimizar(self):
        self.showMinimized()

    def normal(self):
        self.showNormal()
        self.btn_restaurar.hide()
        self.btn_maximizar.show()

    def maximizar(self):
        self.showMaximized()
        self.btn_maximizar.hide()
        self.btn_restaurar.show()

    def activar_opciones(self):
        self.btn_inicio_de_sesion.hide()
        self.btn_inventario.show()
        self.btn_registrar.show()
        self.btn_actualizar.show()
        self.btn_eliminar.show()

    def mover_menu(self):
        width = self.frame_3.width()
        if width == 0:
            new_width = 200
        else:
            new_width = 0

        animacion = QPropertyAnimation(self.frame_3, b"minimumWidth")
        animacion.setDuration(300)
        animacion.setStartValue(width)
        animacion.setEndValue(new_width)
        animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        animacion.start()

    # PARTE DEL INVENTARIO
