
from Errores.errorR import errorR
from Operaciones.evaluar import evaluar
class calcularC:
    
    # calcular c en metodo biseccion, falsa posicion
    def calcular_Biseccion(self,a ,b ):
            return (a+b)/2
    
    def calcular_Falsa_Posicion(self, a, b):

     instancia_evaluar = evaluar()  
     return (((a * instancia_evaluar.evaluar_Funcion(b)) - (b * instancia_evaluar.evaluar_Funcion(a))) / (instancia_evaluar.evaluar_Funcion(b) - instancia_evaluar.evaluar_Funcion(a)))

    def calcular_nuevo_valor(self,x1,x11,fx11,fx1):
      return  ( x11-fx11*((x11-(x1))/(fx11-(fx1))))
    

    def calcular_nuevo_valor_raices_multiples(self,x1):
     isinstancia_evaluar = evaluar()
     return x1-((isinstancia_evaluar.evaluar_Funcion_raices(x1)*isinstancia_evaluar.evaluar_Funcion_raices_derivada(x1,1))/(((isinstancia_evaluar.evaluar_Funcion_raices_derivada(x1,1))**2)-(  isinstancia_evaluar.evaluar_Funcion_raices(x1)*isinstancia_evaluar.evaluar_Funcion_raices_derivada(x1,2)  )))
   
    def calcular_nuevo_valor_raices_multiples(self,x1):
       isinstancia_evaluar = evaluar()
       return x1-isinstancia_evaluar.evaluar_nw_derivada(x1,1)
    
    def calcular_nuevo_valor_nw(self,x1):
       isinstancia_evaluar = evaluar()
       return x1-(isinstancia_evaluar.evaluar_nw_derivada(x1,0)/isinstancia_evaluar.evaluar_nw_derivada(x1,1))

    
