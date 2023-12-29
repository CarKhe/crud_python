from tkinter import *
from menu.htmls import *
class Ventana(Frame,Botones,Labels,Inputs):
    def __init__(self,master=None):
        super().__init__(master,width=680,height=260)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def f_nuevo():
        exit()
   
    
    def create_widgets(self):
        frame1 = Frame(self,bg="#bfdaff")
        frame1.place(x=0,y=0,width=93,height=259)
        
        Botones.agregar_boton("btn_nuevo",frame1,"Nuevo",Botones.salir,"blue","white",5,50,80,30)
        Botones.agregar_boton("btn_modificar",frame1,"Modificar",Botones.salir,"blue","white",5,90,80,30)
        Botones.agregar_boton("btn_eliminar",frame1,"Eliminar",Botones.salir,"blue","white",5,130,80,30)

        frame2 = Frame(self,bg="#d3dde3")
        frame2.place(x=95,y=0,width=150,height=259)
        
        Labels.agregar_label("lbl1",frame2,"ISO 3:",3,5)
        Inputs.agregar_input("txt_iso3",frame2,3,25,140,20)
        Labels.agregar_label("lbl2",frame2,"Country Name:",3,55)
        Inputs.agregar_input("txt_name",frame2,3,75,140,20)
        Labels.agregar_label("lbl4",frame2,"Capital:",3,105)
        Inputs.agregar_input("txt_capital",frame2,3,125,140,20)
        Labels.agregar_label("lbl4",frame2,"Currency Code:",3,155)
        Inputs.agregar_input("txt_code",frame2,3,175,140,20)
        
        Botones.agregar_boton("btn_guardar",frame2,"Guardar",Botones.salir,"green","white",10,210,60,30)
        Botones.agregar_boton("btn_cancelar",frame2,"Cancelar",Botones.salir,"red","white",80,210,60,30)
