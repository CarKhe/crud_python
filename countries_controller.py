from clases.assets import *
from countries import Countries 
from tkinter import messagebox


class CountriesController:
    
    def __init__(self):
        self = self
    
    def create(self,txt_iso3,txt_name,txt_capital,txt_code,btn_save,btn_cancel,btn_create,btn_read,btn_update,btn_delete,obj):
        self.cambiar_estado_inputs("normal",txt_iso3,txt_name,txt_capital,txt_code)
        self.limpiar_inputs(txt_iso3,txt_name,txt_capital,txt_code)
        self.focus_input(obj)
        self.cambiar_estado_bts("normal",btn_save,btn_cancel)
        self.cambiar_estado_bts("disabled",btn_create,btn_read,btn_update,btn_delete)
    
    def cancel(self,txt_iso3,txt_name,txt_capital,txt_code,btn_save,btn_cancel,btn_create,btn_read,btn_update,btn_delete):
        self.limpiar_inputs(txt_iso3,txt_name,txt_capital,txt_code)
        self.cambiar_estado_inputs("disabled",txt_iso3,txt_name,txt_capital,txt_code)
        self.cambiar_estado_bts("disabled",btn_save,btn_cancel)
        self.cambiar_estado_bts("normal",btn_create,btn_read,btn_update,btn_delete)
        
    def save(self,txt_iso3,txt_name,txt_capital,txt_code,btn_save,btn_cancel,btn_create,btn_read,btn_update,btn_delete,obj):
        v = self.obtener_valores(txt_iso3,txt_name,txt_capital,txt_code)
        Countries.inserta_pais(v[0],v[1],v[2],v[3])
        self.limpiar_consultas(obj)
        self.consultar(obj)
        self.limpiar_inputs(txt_iso3,txt_name,txt_capital,txt_code)
        self.cambiar_estado_inputs("disabled",txt_iso3,txt_name,txt_capital,txt_code)
        self.cambiar_estado_bts("disabled",btn_save,btn_cancel)
        self.cambiar_estado_bts("normal",btn_create,btn_read,btn_update,btn_delete)
   

    def delete(self,txt_iso3,txt_name,txt_capital,txt_code,btn_save,btn_cancel,btn_create,btn_read,btn_update,btn_delete,obj):
        selected = self.focus_grid_consulta(obj)
        row,id = self.mostrar_row_seleccionado(obj,selected)
        datos = str(id)+', '+row[0]+', '+row[1]
        r = messagebox.askquestion("Eliminar","Deseas elimianrlo?\n"+datos)
        
        if r == messagebox.YES:
            Countries.elimina_pais(id)
            self.limpiar_consultas(obj)
            self.consultar()
            messagebox.showwarning("Exito!!","Los Datos fueron borrados :)")
            self.cambiar_estado_inputs("disabled",txt_iso3,txt_name,txt_capital,txt_code)
            self.cambiar_estado_bts("disabled",btn_save,btn_cancel)
            self.cambiar_estado_bts("normal",btn_create,btn_read,btn_update,btn_delete)
        else:
            print("Dato no borrado")  
            
            
        
    def cambiar_state_input(obj):
        Inputs.cambiar_state_input(obj,"disabled")
    
    def cambiar_state_input_all(estado,*obj):
        for i in obj:
            Inputs.cambiar_state_input(i,estado)
    
    def focus_input(obj):
        Inputs.focus_input(obj)
        
    def obtener_valor_input(*obj):
        valores = []
        for i in obj:
           val=Inputs.get_valor(i)
           valores.append(val)
        return valores 
        
  
    def limpiar_inputs_all(*obj):
        for i in obj:
            Inputs.limpiar_input(i)
            
    def cambiar_state_btn(state,*obj):
        for i in obj:
            Botones.cambio_state_boton(i,state)
    
    def mostrar_valores(obj,datos):
         for row in datos:
            obj.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4]))
            
    def limpiar_grid(obj):
        for item in obj.get_children():
            obj.delete(item)
    
    def focus_campo_grid(obj):
        return Labels.focus_label(obj)
    
    def mostrar_row(obj,selected):
        x,y = Labels.mostrar_row(obj,selected)
        return x,y      
    
    def salir(self):
        exit()
    
    def limpiar_inputs(self,*obj):
        self.limpiar_inputs_all(*obj)
    
    def focus_input(self):
        self.focus_input(self.txt_iso3)
    
    def cambiar_estado_bts(self,state,*obj):
        self.cambiar_state_btn(state,*obj)
    
    def cambiar_estado_inputs(self,state,*obj):
        self.cambiar_state_input_all(state,*obj)
        
    def consultar(self,obj):
        datos=Countries.consulta_paises()
        self.mostrar_valores(obj,datos)
    
    def limpiar_consultas(self,obj):
        self.limpiar_grid(obj)
    
    def obtener_valores(self,*obj):
        valores = self.obtener_valor_input(*obj)
        return valores
    
    def focus_grid_consulta(self,obj):
        v=self.focus_campo_grid(obj)
        return v
    
    def mostrar_row_seleccionado(self,obj,selected):
        v,t = self.mostrar_row(obj,selected)
        return v,t
            
      
    