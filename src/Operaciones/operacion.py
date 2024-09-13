from Operaciones.evaluar import evaluar

class operacion:

    instancia_evaluar = evaluar
    def evaluar_funciones(self, a, b ):
       if evaluar.evaluar_Funtcion(a)* evaluar.evaluar_Funtcion(b) == 0:
           print("Es la raiz")
           
       if evaluar.evaluar_Funtcion(a)* evaluar.evaluar_Funtcion(b) <0:
           print(" continuamos ")
          
       if evaluar.evaluar_Funtcion(a)* evaluar.evaluar_Funtcion(b) > 0:
           print ("solicitar nuevo valor")

       return evaluar.evaluar_Funtcion(a)* evaluar.evaluar_Funtcion(b)
    



     
       
    
           
           

