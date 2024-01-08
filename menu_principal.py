from pantalla import *
from clases.assets import *
from tkinter import ttk
from countries_controller import CountriesController as Cc

class MenuPrincipal(Pantalla,Cc):
    def __init__(self,titulo,w,h):
        Pantalla.__init__(self,titulo,w,h)
        Cc.__init__(self)
        self.create_widgets()
        Cc.consultar(self,self.grid)
        self.ddn()
        
    def salir(self):
        exit()
    
    def ddn(self):
        Cc.cambiar_state_input_all("disabled",self.txt_iso3,self.name,self.capital,self.code)
        Cc.cambiar_state_btn("disabled",self.btn_save,self.btn_cancel)
        Cc.cambiar_state_btn("normal",self.btn_create,self.btn_read,self.btn_update,self.btn_delete)
        self.btn_save.configure(text="Save",bg="green",command=self.create)
        
    def nd(self):
        Cc.cambiar_state_btn("normal",self.btn_save,self.btn_cancel)
        Cc.cambiar_state_btn("disabled",self.btn_create,self.btn_read,self.btn_update,self.btn_delete)
    
    def ndi(self):
        Cc.cambiar_state_input_all("normal",self.txt_iso3,self.name,self.capital,self.code,self.btn_save,self.btn_cancel)
        Cc.cambiar_state_btn("disabled",self.btn_create,self.btn_read,self.btn_update,self.btn_delete)
        Cc.limpiar_inputs_all(self.txt_iso3,self.name,self.capital,self.code)
    
        
    def create(self):
        Cc.cambiar_state_input_all("normal",self.txt_iso3,self.name,self.capital,self.code)
        Cc.limpiar_inputs_all(self.txt_iso3,self.name,self.capital,self.code)
        Cc.focus_input(self.txt_iso3)
        self.nd()
    
    def cancel(self):
        Cc.limpiar_inputs_all(self.txt_iso3,self.name,self.capital,self.code)
        self.btn_save.configure(text="Save",bg="green",command=self.create)
        self.ddn()
        
    def save(self):
        v = Cc.obtener_valor_input(self.txt_iso3,self.name,self.capital,self.code)
        Cc.insertar(self,v[0],v[1],v[2],v[3])
        Cc.limpiar_grid(self,self.grid)
        Cc.consultar(self,self.grid)
        Cc.limpiar_inputs_all(self.txt_iso3,self.name,self.capital,self.code)
        self.ddn()
    
    def delete(self):
        selected = Cc.focus_campo_grid(self.grid)
        row,id = Cc.mostrar_row(self.grid,selected)
        Cc.pregunta_eliminar(self,id,row,self.grid)
        self.ddn()
        
    def pre_update(self):
        selected = Cc.focus_campo_grid(self.grid)
        row,id = Cc.mostrar_row(self.grid,selected)
        self.ndi()
        Cc.pre_actualizar(id,row,self.txt_iso3,self.name,self.capital,self.code)
        self.btn_save.configure(text="Modificar",bg="orange",command= lambda: self.act(id))
    
    
    def act(self,id):
        v = Cc.obtener_valor_input(self.txt_iso3,self.name,self.capital,self.code)
        Cc.actualizar(self,v[0],v[1],v[2],v[3],id)
        Cc.limpiar_grid(self,self.grid)
        Cc.consultar(self,self.grid)
        Cc.limpiar_inputs_all(self.txt_iso3,self.name,self.capital,self.code)
        self.ddn()
            
    def read(self):
        Cc.preguntar_valor_buscar(self)
 
    def create_widgets(self):
        frame1 = Frame(self,bg="#bfdaff")
        frame1.place(x=0,y=0,width=93,height=259)
        
        self.btn_create = Botones.agregar_boton("btn_create",frame1,"Create",self.create,"blue","white",5,50,80,30)
        self.btn_read = Botones.agregar_boton("btn_read",frame1,"Read",self.read,"blue","white",5,90,80,30)
        self.btn_update = Botones.agregar_boton("btn_update",frame1,"Update",self.pre_update,"blue","white",5,130,80,30)
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
        
        self.grid['selectmode'] = 'browse'