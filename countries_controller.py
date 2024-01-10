from clases.assets import *
from clases.validacion import Validacion
from countries import Countries 
from tkinter import messagebox
from tkinter.simpledialog import askstring


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
        v0 = str(v0).upper()
        v1 = str(v1).capitalize()
        v2 = str(v2).capitalize()
        v3 = str(v3).upper()
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
    
    def preguntar_valor_buscar(self):
        pais = askstring('pais','¿Qué pais quieres buscar?')
        datos=self.buscar_pais(pais)
        if datos != None:
            rst = self.dividir_parametros(datos)
            messagebox.showinfo('Resultado', 'Resultado:\n {}'.format(rst))
        else:
            messagebox.showinfo('Resultado', 'No Hay Resultado')

    def pre_actualizar(id,row,*obj):
        if id != '':
            v=0
            for i in obj:
                Labels.mostrar_input(i,row[v])
                v+=1 
                
        else:
            print("No hay valor")
    
    def actualizar(self,v0,v1,v2,v3,id):
        self.modifica_pais(v0,v1,v2,v3,id)
    
    
    def validar_campos(self,v,id=0):
        v0_val = Validacion.es_alfabetico(v[0],3)
        v1_val = Validacion.es_alfabetico(v[1],64)
        v2_val = Validacion.es_alfabetico(v[2],64)
        v3_val = Validacion.es_alfabetico(v[3],3)
        if v0_val & v1_val & v2_val & v3_val:
            if id == 0:
                self.insertar(v[0],v[1],v[2],v[3])
                return True
            else:
                self.actualizar(v[0],v[1],v[2],v[3],id)
                return True
        else:
            return False
    
    
    def mensaje_insertar(res): 
        if res:
            messagebox.showinfo('Mensaje', '¡Valor Guardado!')
        else:
            messagebox.showinfo('Mensaje', '¡Error al Insertar, Revisa tus datos!')
                
        
 
 
    

    
    
    
    
   