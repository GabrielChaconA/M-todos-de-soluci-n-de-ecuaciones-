from Operaciones.evaluar import evaluar
class operacionesC:
    
    """ condiciones """
    def operacionC(self, a, c):
        if evaluar.evaluar_Funtcion(a)* evaluar.evaluar_Funtcion(c) == 0:
           print("Es la raiz")
           
        if evaluar.evaluar_Funtcion(a)* evaluar.evaluar_Funtcion(c) <0:
           print(" continuamos ")
          
        if evaluar.evaluar_Funtcion(a)* evaluar.evaluar_Funtcion(c)> 0:
           print ("solicitar nuevo valor")

        return evaluar.evaluar_Funtcion(a)* evaluar.evaluar_Funtcion(c)
     