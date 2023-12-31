from tkinter import *

class Pantalla(Frame):
    def __init__(self,titulo,w,h):
        root = Tk()
        root.wm_title(titulo)
        super().__init__(width=w,height=h)
        self.pack()
        
        
        