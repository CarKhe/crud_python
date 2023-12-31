from tkinter import *
from tkinter import ttk
from countries import *

class Botones:
    def agregar_boton(btn_name,frame,text,command,bg,fg,x,y,width,height):
          btn_name =  Button(frame,text=text,command=command, bg=bg,fg=fg)
          btn_name.place(x=x,y=y,width=width,height=height)
          

class Labels:
    def agregar_label(name,frame,text,x,y):
          name = Label(frame,text=text)
          name.place(x=x,y=y)

class Inputs:
    def agregar_input(name,frame,x,y,width,height):
          name = Entry(frame)
          name.place(x=x,y=y,width=width,height=height)
          
class Tree_Class:
    def ttk_columnas(self,cant):
        val = 1
        col = ""
        columns = []
        while val<=cant:
            col =f"col{val}"
            columns.append(col)
            val += 1
        columns = tuple(columns)
        ttk.Treeview(self,columns=columns)

