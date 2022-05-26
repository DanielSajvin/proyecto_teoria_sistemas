import sqlite3



class Comunicacion:
    def __int__(self):
        self.conexion = sqlite3.connect('data_base.db')

    def insertar_producto(self, codigo, producto, costo, precio, existencia):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO productos (CODIGO, PRODUCTO, COSTO, PRECIO, EXISTENCIA)
        VALUES ('{}', '{}', '{}', '{}', '{}')'''.format(codigo, producto, costo, precio, existencia)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM productos"
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_producto):
        cursor = self.conexion.cursor()
        db = '''SELECT * FROM productos WHERE PRODUCTO = {}'''.format(nombre_producto)
        cursor.execute(db)
        nombrex = cursor.fetchall()
        cursor.close()
        return nombrex

    def elimina_producto(self, nombre):
        cursor = self.conexion.cursor()
        db = '''DELETE FROM productos WHERE PRODUCTO = {}'''.format(nombre)
        cursor.execute(db)
        self.conexion.commit()
        cursor.close()

    def actualiza_productos(self, idd, codigo, producto, costo, precio, existencia):
        cursor = self.conexion.cursor()
        db = '''UPDATE productos SET CODIGO = '{}', PRODUCTO = '{}', COSTO = '{}', PRECIO = '{}', EXISTENCIA = '{}' 
        WHERE ID = '{}' '''.format(codigo, producto, costo, precio, existencia, idd)
        cursor.execute(db)
        x = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return x
