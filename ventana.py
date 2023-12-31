from tkinter import *
from tkinter import ttk
from clases.assets import *
from countries import Countries as ct

class Ventana(Frame,ct):
    def __init__(self,master=None):
        super().__init__()
        super().__init__(master,width=685,height=260)
        self.master = master
        self.pack()
        self.create_widgets()
    
    
            
            
    def salir(self):
        exit()
        
   
    
    def create_widgets(self):
        frame1 = Frame(self,bg="#bfdaff")
        frame1.place(x=0,y=0,width=93,height=259)
        
        Botones.agregar_boton("btn_create",frame1,"Create",self.salir,"blue","white",5,50,80,30)
        Botones.agregar_boton("btn_read",frame1,"Read",self.salir,"blue","white",5,90,80,30)
        Botones.agregar_boton("btn_update",frame1,"Update",self.salir,"blue","white",5,130,80,30)
        Botones.agregar_boton("btn_delete",frame1,"Delete",self.salir,"blue","white",5,170,80,30)

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
        
        Botones.agregar_boton("btn_guardar",frame2,"Guardar",self.salir,"green","white",10,210,60,30)
        Botones.agregar_boton("btn_cancelar",frame2,"Cancelar",self.salir,"red","white",80,210,60,30)
        
        self.grid = ttk.Treeview(self,columns=("col1", "col2", "col3", "col4"))
        
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)
        
        self.grid.heading("#0",text="Id", anchor=CENTER)
        self.grid.heading("col1",text="ISO3", anchor=CENTER)
        self.grid.heading("col2",text="Country Name", anchor=CENTER)
        self.grid.heading("col3",text="Capital", anchor=CENTER)
        self.grid.heading("col4",text="Currency Code", anchor=CENTER)
        
        self.grid.place(x=247,y=0,width=420,height=259)
        
        self.grid.insert("",END,text="1",values=("ARG","Argentina","Buenos Aires","ARS"))
        
        
      
        
        