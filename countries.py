from conexion.conexion import MysqlConnection as MsqlC
from tkinter import ttk
from clases.assets import *

class Countries(MsqlC):
    tabla = "countries"
    columnas = "(ISO3, CountryName, Capital, CurrencyCode)"

    def __init__(self):
        super().__init__()


    def __str__(self):
        aux = self.to_list_cmd(f"SELECT * FROM {self.tabla}")
        return aux
    
    def consulta_paises(self):
        datos = self.search_all(f"SELECT * FROM {self.tabla}")
        return datos
    
    def buscar_pais(self,val):
        condicion = "CountryName='{}'".format(val)
        datos = self.search_select_columns(self.tabla,condicion,"ISO3","CountryName","Capital","CurrencyCode")  
        return datos
    
    def buscar_pais_id(self,val):
        condicion = "Id={}".format(val)
        datos = self.search_all_by_condition("countries",condicion)  
        return datos
    
    def inserta_pais(self,ISO3, CountryName, Capital, CurrencyCode):
        valores = "('{}','{}','{}','{}')".format(ISO3, CountryName, Capital, CurrencyCode)
        n = self.insert(self.tabla,self.columnas,valores)
        return n

    def elimina_pais(self,id):
        condicion = "Id={}".format(id)
        n = self.delete_by_id(self.tabla,condicion)
        return n   

    def modifica_pais(self, ISO3, CountryName, Capital, CurrencyCode,id):
        cond = "Id={}".format(id)
        val="ISO3='{}', CountryName='{}', Capital='{}',CurrencyCode='{}'".format(ISO3, CountryName, Capital, CurrencyCode)
        n = self.update_row(self.tabla,val,cond)
        return n  
    
    def dividir_parametros(self,datos):
        rst=''
        campos=("ISO3", "CountryName", "Capital", "CurrencyCode")
        v=0
        for i in datos:
            rst = rst + f'{campos[v]} : {i}\n'
            v+=1
        return rst
    
   
    
    
