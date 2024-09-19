
from Operaciones.evaluar import evaluar
from Operaciones.Calcular.calcular_Nuevo_Valor import calcular_Nuevo_Valor
from Errores.errorR import errorR
class tabla_Falsa_posicion:

     def tabla_de_valores_Falsa_posicion(self):
        #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcular_Nuevo_Valor()
        instance_errorR = errorR()
        #variables de valores de tabla ( iniciales )
        a = int(input("Escriba valor a: "))
        b = int(input("Escriba valor b: "))
        c_Anterior = 0
        error = 0

        print("a | b | f(a)| f(b)| c | f(c) |Error relativo")
        flag = True 
        while(flag):
         #valores de la tabal, actualizables 
         c = instance_calcularC.calcular_Falsa_Posicion(a,b)
         fa = instance_evaluar.evaluar_Funcion(a)
         fb = instance_evaluar.evaluar_Funcion(b)
         fc = instance_evaluar.evaluar_Funcion(c) 
         if a !=0 :
            error = instance_errorR .errorR(c,c_Anterior)
            if error <= instance_errorR .error_Tolerable:
               print("fin ")
               break

         print("{} | {} | {} |  {}| {} | {} | {}| ".format(a,b, fa, fb, c , fc, error))
         if fa*fb == 0:
            print("Es la raziz")
            flag = False
         if  fa*fb < 0:
             if fa*fc == 0:
              print("Es la raziz")
              flag = False
              
             
             if  fa*fc < 0:
                b = c
  
                
             if  fa*fc >0:
                a =c
               
            
         if  fa*fb >0:
           print(" necesitas otro valores")
           a = int(input("Escriba a: "))
           b = int(input("Escriba b: "))

         c_Anterior = c
     