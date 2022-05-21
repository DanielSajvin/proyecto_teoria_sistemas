from tkinter import ttk
from tkinter import *
import sqlite3


class Inventory:

    db_name = 'dataabase.db'

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
            return result

    def get_products(self):
        records = self.tree.get_children()
        # Limpiando la tabla
        for elemnt in records:
            self.tree.delete(elemnt)

        query = 'SELECT * FROM Inventario ORDER BY Producto DESC'
        db_rows = self.run_query(query)

        # Rellenando los datos
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=[2])

    def __init__(self, window):
        self.wind = window
        self.wind.title('Módulo Inventario')

        # Crear Frame o contenedor, para que vaya dentro el contenido
        frame = LabelFrame(self.wind, text='Ingresa un Nuevo Producto')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Caja para ingresar producto
        Label(frame, text='Nombre del Producto: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        # Caja para ingresar cantidad producto
        Label(frame, text='Cantidad producto: ').grid(row=2, column=0)
        self.product_quantity = Entry(frame)
        self.product_quantity.grid(row=2, column=1)

        # Caja para ingresar costo unitario
        Label(frame, text='Costo unitario: ').grid(row=3, column=0)
        self.unit_cost = Entry(frame)
        self.unit_cost.grid(row=3, column=1)

        # Boton agregar producto
        ttk.Button(frame, text='Agregar producto').grid(row=4, columnspan=2, sticky=W + E)

        # Tabla para mostrar el inventario
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=5, column=0, columnspan=2)
        self.tree.heading('#0', text='Producto', anchor=CENTER)
        self.tree.heading('#1', text='Costo', anchor=CENTER)

        self.get_products()
