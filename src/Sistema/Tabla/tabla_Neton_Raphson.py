
from Operaciones.evaluar import evaluar
from Operaciones.Calcular.calcular_Nuevo_Valor import calcular_Nuevo_Valor
from Errores.errorR import errorR

class tabla_Neton_Raphson:
    def tabla_Neton_Raphson(self):
          #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcular_Nuevo_Valor()
        instance_errorR = errorR()
        #variables de valores de tabla ( iniciales )
        x1 = 1
        i = 0
      
        print("i | x1 | f(x1) | f´(x1) | x1+1 | Error relativo")
        flag = True 
        if instance_evaluar.evaluar_nw_derivada(x1,0) == 0:
            print(instance_evaluar.evaluar_nw_derivada(x1,0)+ " es la raiz")
        else:
         while(flag):
          x11 =instance_calcularC.calcular_nuevo_valor_nw(x1)
          error = instance_errorR.errorR(x11,x1)
       
         
          print("{} | {} | {} | {} |  {} | {}% | ".format(i, x1, instance_evaluar.evaluar_nw_derivada(x1,0),  instance_evaluar.evaluar_nw_derivada(x1,1),x11, error))
          x1 = x11
        
          if error <= instance_errorR.error_Tolerable:
               print("fin ")
               break
        
          i=i+1

