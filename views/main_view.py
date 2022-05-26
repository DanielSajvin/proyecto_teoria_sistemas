from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QHeaderView
from PyQt5 import QtCore, QtWidgets
from inventory import Comunicacion
from PyQt5.uic import loadUi


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
        #self.base_datos = Comunicacion()
        # -------------------
        #self.actualizar.clicked.connect(self.actualiza_productos)
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

    def mostrar_producto(self):
        datos = self.data_base.mostrar_productos()
        i = len(datos)
        self.productos.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.idd = row[0]
            self.productos.serItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.productos.serItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.productos.serItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.productos.serItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.productos.serItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))
            tablerow +=1
            self.actualizar.setText("")
            self.btn_registrarse.setText("")
            self.pushButton_6.setText("")

    def registrar_producto(self):
        codigo = self.lineEdit_reg_aso_nombre_2.text().upper()
        producto = self.lineEdit_reg_aso_nombre_3.text().upper()
        costo = self.lineEdit_reg_aso_nombre_4.text().upper()
        precio = self.lineEdit_reg_aso_nombre_5.text().upper()
        existencia = self.lineEdit_reg_aso_nombre_6.text().upper()
        if codigo != '' and producto != '' and costo != '' and precio != '' and existencia != '':
            self.data_base.insertar_producto(codigo, producto, costo, precio, existencia)
            self.btn_registrarse.setText('Productos Registrados')
            self.lineEdit_reg_aso_nombre_2.clear()
            self.lineEdit_reg_aso_nombre_3.clear()
            self.lineEdit_reg_aso_nombre_4.clear()
            self.lineEdit_reg_aso_nombre_5.clear()
            self.lineEdit_reg_aso_nombre_6.clear()
        else:
            self.btn_registrarse.setText('Hay espacios vacios')
