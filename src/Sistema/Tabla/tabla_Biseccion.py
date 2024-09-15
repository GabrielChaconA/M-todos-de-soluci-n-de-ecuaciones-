


class tabla_Biseccion:
    """ Esta tabla contiene los valores y la ejecucion del metodo "Biseccion" """
    def tabla_de_valores_Biseccion(self):
    
        #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcularC()
        instance_errorR = errorR()
        #variables de valores de tabla ( iniciales )
        a = 0
        b = 1
        c_Anterior = 0
        error = 0


     

        print("a | b | f(a)| f(b)| c | f(c) |Error relativo")
        flag = True 
        while(flag):
         #valores de la tabal, actualizables 
         c = instance_calcularC.calcular_Biseccion(a, b)
         fa = instance_evaluar.evaluar_Funcion(a)
         fb = instance_evaluar.evaluar_Funcion(b)
         fc = instance_evaluar.evaluar_Funcion(c) 
         if a !=0 :
            error = instance_errorR .errorRelativo(c,c_Anterior)
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
            print(" necesitas otro valor de a")
            flag = False

         c_Anterior = c