import re
class Validacion:
    def es_entero(variable):
        try:
            int(variable)
            return True
        except:
            return False
    
    def es_flotante(variable):
        try:
            float(variable)
            return True
        except:
            return False
    
    def es_string(variable):
        if isinstance(variable, str):
           return True
        else:
           return False
    
    def es_alfanumerico(variable,limite):
        try:
            patron = r"^[\w\s]{,"+str(limite)+"}$"
            resultado = re.findall(patron,variable)
            if resultado == []:
                return False
            else:
                return True
        except:
            return False
    
    def es_correo(variable):
        try:
            patron = r"^[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            resultado =re.findall(patron, variable)
            if resultado == []:
                return False
            else:
                return True
        except:
            return False
    
    def letras_longitud(dato,longitud):
        try:
            #Expresion donde marca que de inicio a fin de la expresion solo mayusculas y limite deseado
            patron = r"^[a-zA-Z]{"+str(longitud)+"}$"
            resultado = re.findall(patron,dato)
            if resultado == []:
                return False
            else:
                return True
        except:
            return False

datos = [123, "asd", "AA AW", "----", -5, "1.60","Aqqwe !!wDWq","aA","carlos@erdf.web","carlos@gamil.e"]
for dato in datos:
	print("'{}' resultado: {}".format(dato, Validacion.es_correo(dato)))


