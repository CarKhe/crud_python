from tkinter import *
from ventana import *


class Menu:
    def main():
        root = Tk()
        root.wm_title("Crud Python Mysql")
        app = Ventana(root)
        app.mainloop()

if __name__ == '__main__': 
    Menu.main()