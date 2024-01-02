from clases.assets import *
from countries import Countries 
from tkinter import messagebox

class CountriesController(Countries):
    def __init__(self):
        Countries.__init__(self)
   
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
    
            
    def limpiar_grid(self,obj):
        for item in obj.get_children():
            Labels.limpiar_grid(obj,item)
    
    def focus_campo_grid(obj):
        return Labels.focus_label(obj)
    
    def mostrar_row(obj,selected):
        x,y = Labels.mostrar_row(obj,selected)
        return x,y      
            
    def consultar(self,obj):
        datos=self.consulta_paises()
        for row in datos:
            Labels.mostrar_valor(obj,row)
    
    def insertar(self,v0,v1,v2,v3):
        self.inserta_pais(v0,v1,v2,v3)
    
    def pregunta_eliminar(self,id,row,obj):
        datos = str(id)+', '+row[0]+', '+row[1]
        r = messagebox.askquestion("Eliminar","¿Deseas elimianrlo?\n"+datos)
        if r == messagebox.YES:
            self.elimina_pais(id)
            self.limpiar_grid(obj)
            self.consultar(obj)
            messagebox.showwarning("Exito!!","Los Datos fueron borrados :)")
        else:
            print("Dato no borrado")
    