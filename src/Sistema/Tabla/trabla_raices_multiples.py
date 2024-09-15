
from Operaciones.evaluar import evaluar
from Operaciones.Calcular.calcular_Nuevo_Valor import calcular_Nuevo_Valor
from Errores.errorR import errorR
class tabla_raices_multiples:
    def tabla_raices_multiples(self):
          #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcular_Nuevo_Valor()
        instance_errorR = errorR()
        #variables de valores de tabla ( iniciales )
        x1 = 0
        i = 0
      
        print("i | x1 | f(x1) | f´(x1) | f´´(x1)| x1+1 | Error relativo")
        flag = True 
        while(flag):
         x11 =instance_calcularC.calcular_nuevo_valor_raices_multiples(x1)
         error = instance_errorR.errorR(x11,x1)
         print("{} | {} | {} | {} |  {} | {} | {}% | ".format(i, x1, instance_evaluar.evaluar_Funcion_raices_derivada(x1,0), instance_evaluar.evaluar_Funcion_raices_derivada(x1,1),instance_evaluar.evaluar_Funcion_raices_derivada(x1,2),x11, error))
         x1 = x11
        
        
         if error <= instance_errorR.error_Tolerable:
               print("fin ")
               break
        
         i=i+1

