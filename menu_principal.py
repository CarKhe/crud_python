from pantalla import *
from clases.assets import *
from tkinter import ttk
from tkinter import messagebox
from countries import Countries 
from countries_controller import CountriesController as Cc

class MenuPrincipal(Pantalla,Countries):
    def __init__(self,titulo,w,h):
        Pantalla.__init__(self,titulo,w,h)
        Countries.__init__(self)
        self.create_widgets()
        self.consultar()
        self.cambiar_estado_inputs("disabled",self.txt_iso3,self.name,self.capital,self.code)
        self.cambiar_estado_bts("disabled",self.btn_save,self.btn_cancel)
        self.cambiar_estado_bts("normal",self.btn_create,self.btn_read,self.btn_update,self.btn_delete)
        
    def salir(self):
        exit()
    
    def limpiar_inputs(self,*obj):
        Cc.limpiar_inputs_all(*obj)
    
    def focus_input(self):
        Cc.focus_input(self.txt_iso3)
    
    def cambiar_estado_bts(self,state,*obj):
        Cc.cambiar_state_btn(state,*obj)
    
    def cambiar_estado_inputs(self,state,*obj):
        Cc.cambiar_state_input_all(state,*obj)
        
    def consultar(self):
        datos=self.consulta_paises()
        Cc.mostrar_valores(self.grid,datos)
    
    def limpiar_consultas(self,obj):
        Cc.limpiar_grid(obj)
    
    def obtener_valores(self,*obj):
        valores = Cc.obtener_valor_input(*obj)
        return valores
    
    def focus_grid_consulta(self,obj):
        v=Cc.focus_campo_grid(obj)
        return v
    
    def mostrar_row_seleccionado(self,obj,selected):
        v,t = Cc.mostrar_row(obj,selected)
        return v,t
            
    def create(self):
        self.cambiar_estado_inputs("normal",self.txt_iso3,self.name,self.capital,self.code)
        self.limpiar_inputs(self.txt_iso3,self.name,self.capital,self.code)
        self.focus_input()
        self.cambiar_estado_bts("normal",self.btn_save,self.btn_cancel)
        self.cambiar_estado_bts("disabled",self.btn_create,self.btn_read,self.btn_update,self.btn_delete)
    
    def cancel(self):
        self.limpiar_inputs(self.txt_iso3,self.name,self.capital,self.code)
        self.cambiar_estado_inputs("disabled",self.txt_iso3,self.name,self.capital,self.code)
        self.cambiar_estado_bts("disabled",self.btn_save,self.btn_cancel)
        self.cambiar_estado_bts("normal",self.btn_create,self.btn_read,self.btn_update,self.btn_delete)
        
    def save(self):
        v = self.obtener_valores(self.txt_iso3,self.name,self.capital,self.code)
        self.inserta_pais(v[0],v[1],v[2],v[3])
        self.limpiar_consultas(self.grid)
        self.consultar()
        self.limpiar_inputs(self.txt_iso3,self.name,self.capital,self.code)
        self.cambiar_estado_inputs("disabled",self.txt_iso3,self.name,self.capital,self.code)
        self.cambiar_estado_bts("disabled",self.btn_save,self.btn_cancel)
        self.cambiar_estado_bts("normal",self.btn_create,self.btn_read,self.btn_update,self.btn_delete)
    
    def delete(self):
        selected = self.focus_grid_consulta(self.grid)
        row,id = self.mostrar_row_seleccionado(self.grid,selected)
        datos = str(id)+', '+row[0]+', '+row[1]
        r = messagebox.askquestion("Eliminar","Deseas elimianrlo?\n"+datos)
        
        if r == messagebox.YES:
            self.elimina_pais(id)
            self.limpiar_consultas(self.grid)
            self.consultar()
            messagebox.showwarning("Exito!!","Los Datos fueron borrados :)")
            self.cambiar_estado_inputs("disabled",self.txt_iso3,self.name,self.capital,self.code)
            self.cambiar_estado_bts("disabled",self.btn_save,self.btn_cancel)
            self.cambiar_estado_bts("normal",self.btn_create,self.btn_read,self.btn_update,self.btn_delete)
        else:
            print("Dato no borrado")
            
        
 
    def create_widgets(self):
        frame1 = Frame(self,bg="#bfdaff")
        frame1.place(x=0,y=0,width=93,height=259)
        
        self.btn_create = Botones.agregar_boton("btn_create",frame1,"Create",self.create,"blue","white",5,50,80,30)
        self.btn_read = Botones.agregar_boton("btn_read",frame1,"Read",self.salir,"blue","white",5,90,80,30)
        self.btn_update = Botones.agregar_boton("btn_update",frame1,"Update",self.salir,"blue","white",5,130,80,30)
        self.btn_delete = Botones.agregar_boton("btn_delete",frame1,"Delete",self.delete,"blue","white",5,170,80,30)

        frame2 = Frame(self,bg="#d3dde3")
        frame2.place(x=95,y=0,width=150,height=259)
        
        Labels.agregar_label("lbl1",frame2,"ISO 3:",3,5)
        self.txt_iso3 = Inputs.agregar_input("txt_iso3",frame2,3,25,140,20,"normal")
        Labels.agregar_label("lbl2",frame2,"Country Name:",3,55)
        self.name = Inputs.agregar_input("txt_name",frame2,3,75,140,20,"normal")
        Labels.agregar_label("lbl4",frame2,"Capital:",3,105)
        self.capital = Inputs.agregar_input("txt_capital",frame2,3,125,140,20,"normal")
        Labels.agregar_label("lbl4",frame2,"Currency Code:",3,155)
        self.code = Inputs.agregar_input("txt_code",frame2,3,175,140,20,"normal")
        
        self.btn_save = Botones.agregar_boton("btn_save",frame2,"Save",self.save,"green","white",10,210,60,30)
        self.btn_cancel = Botones.agregar_boton("btn_cancel",frame2,"Cancel",self.cancel,"red","white",80,210,60,30)
        
        frame3 = Frame(self,bg="#bfdaff")
        frame3.place(x=255,y=0,width=420,height=259)
        
        
        self.grid = ttk.Treeview(frame3,columns=("col1", "col2", "col3", "col4"))
        
        self.grid.column("#0",width=60)
        self.grid.column("col1",width=70, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)
        
        self.grid.heading("#0",text="Id", anchor=CENTER)
        self.grid.heading("col1",text="ISO3", anchor=CENTER)
        self.grid.heading("col2",text="Country Name", anchor=CENTER)
        self.grid.heading("col3",text="Capital", anchor=CENTER)
        self.grid.heading("col4",text="Currency Code", anchor=CENTER)
        
        self.grid.pack(side=LEFT, fill=Y,)
        
        scroll_bar = Scrollbar(frame3, orient=VERTICAL) 
        scroll_bar.pack( side = RIGHT, fill = Y ) 
        self.grid.config(yscrollcommand=scroll_bar.set)
        scroll_bar.config( command = self.grid.yview ) 
        