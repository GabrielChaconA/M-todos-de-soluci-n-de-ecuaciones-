
from Operaciones.evaluar import evaluar
from Operaciones.Calcular.calcularC import calcularC
from Errores.errorR_PuntoFijo import errorR_PuntoFijo
class tabla_Punto_Fijo :
    def tabla_Punto_Fijo(self):
        #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcularC()
        instance_errorR = errorR_PuntoFijo()
        #variables de valores de tabla ( iniciales )
        x1 = 0
        i = 0
      
        print("i | x1 | f(x1)| x1 +1 | Error relativo")
        flag = True 
        while(flag):
         x2=instance_evaluar.evaluar_Funcion_derivada(x1)
         error = instance_errorR.errorR_PuntoFijo(x1,x2)
         
         print("{} | {} | {}     | {}      | {}% | ".format(i,x1, instance_evaluar.evaluar_Funcion_PF(x1), x2, error))
         x1=x2
         if error < instance_errorR.error_Tolerable:
               print("fin ")
               break
 
         i=i+1