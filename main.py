from tkinter import *
from inventory import Inventory


if __name__ == '__main__':
    window = Tk()
    application = Inventory(window)
    window.mainloop()
