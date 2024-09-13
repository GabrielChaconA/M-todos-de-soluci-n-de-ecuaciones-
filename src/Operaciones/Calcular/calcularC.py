
from Errores.errorR import errorR
from Operaciones.evaluar import evaluar
class calcularC:
    
    # calcular c en metodo biseccion, falsa posicion
    def calcular_Biseccion(self,a ,b ):
            return (a+b)/2
    
    def calcular_Falsa_Posicion(self, a, b):

     instancia_evaluar = evaluar()
     return (((a * instancia_evaluar.evaluar_Funcion(b)) - (b * instancia_evaluar.evaluar_Funcion(a))) / (instancia_evaluar.evaluar_Funcion(b) - instancia_evaluar.evaluar_Funcion(a)))

