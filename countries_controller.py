from clases.assets import *

class CountriesController:
        
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
            
            
    
    