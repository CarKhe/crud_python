from conexion.conexion import MysqlConnection as MsqlC

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

    def buscar_pais(self,id):
        condicion = "Id={}".format(id)
        datos = self.search_all_by_id("countries",condicion)  
        return datos
    
    def inserta_pais(self,ISO3, CountryName, Capital, CurrencyCode):
        valores = "({},'{}','{}','{}')".format(ISO3, CountryName, Capital, CurrencyCode)
        n = self.insert(self.tabla,self.columnas,valores)
        return n    

    def elimina_pais(self,id):
        condicion = "Id={}".format(id)
        n = self.delete_by_id(self.tabla,condicion)
        return n   

    def modifica_pais(self,id, ISO3, CountryName, Capital, CurrencyCode):
        valores="ISO3='{}', CountryName='{}', Capital='{}',CurrencyCode='{}'".format(ISO3, CountryName, Capital, CurrencyCode)
        condicion = "Id={}".format(id)
        n = self.update(self.tabla,valores,condicion)
        return n   
    
    
