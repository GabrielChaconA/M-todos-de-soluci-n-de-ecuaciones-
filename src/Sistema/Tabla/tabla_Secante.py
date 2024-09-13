
from Operaciones.evaluar import evaluar
from Operaciones.Calcular.calcularC import calcularC
from Errores.errorR_secante import errorR_secante

class tabla_Secante:
    def tabla_Secante(self):
        
        #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcularC()
        instance_errorR = errorR_secante()
        #variables de valores de tabla ( iniciales )
        x1 = 0
        x11= 1
        i = 0
      
        print("i | x1 | x1 +1 | f(x1) | f(x1+1)| x1+2 | Error relativo")
        flag = True 
        while(flag):
         x2 =instance_calcularC.calcular_nuevo_valor(x1,x11,instance_evaluar.evaluar_Funcion_secante(x11),instance_evaluar.evaluar_Funcion_secante(x1))
         error = instance_errorR.errorR_secante(x2,x11)
       
         
         print("{} | {} | {} | {} |  {} | {} | {}% | ".format(i, x1, x11, instance_evaluar.evaluar_Funcion_secante(x1),instance_evaluar.evaluar_Funcion_secante(x11),x2, error))
         x1 = x11
         x11 = x2
        
        
         if error <= instance_errorR.error_Tolerable:
               print("fin ")
               break
        
         i=i+1




