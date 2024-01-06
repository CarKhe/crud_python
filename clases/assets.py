from tkinter import *
from tkinter import ttk
from countries import *

class Botones:
 
    def agregar_boton(obj,frame,text,command,bg,fg,x,y,width,height):
          obj =  Button(frame,text=text,command=command, bg=bg,fg=fg)
          obj.place(x=x,y=y,width=width,height=height)
          return obj
    
    def cambio_state_boton(obj,state):
        obj.configure(state=state)   
    
    def cambio_btn_modificar(obj,command):
        obj.configure(text="Modificar",bg="orange",command=command)
    

class Labels:
    
    def agregar_label(obj,frame,text,x,y):
          obj = Label(frame,text=text)
          obj.place(x=x,y=y)
          return obj
    def focus_label(obj):
        return obj.focus()
    
    def mostrar_row(obj,selected):
        val = obj.item(selected,'values')
        txt = obj.item(selected,'text')
        return val, txt
    
    def mostrar_valor(obj,row):
        obj.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4]))
    
    def limpiar_grid(obj,item):
        obj.delete(item)
    
    def mostrar_input(obj,value):
        obj.insert(0,value)
        
class Inputs:
    def agregar_input(obj,frame,x,y,width,height,state):
          obj = Entry(frame)
          obj.place(x=x,y=y,width=width,height=height)
          obj.configure(state=state)
          return obj
      
    def cambiar_state_input(obj,state):
        obj.configure(state=state)
        
    def limpiar_input(obj):
        obj.delete(0,END)
    
    def focus_input(obj):
        obj.focus()
    
    def get_valor(obj):
        return obj.get()
    
   

