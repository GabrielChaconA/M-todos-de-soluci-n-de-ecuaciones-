import sympy as sp
from Operaciones.evaluar import evaluar
from Operaciones.Calcular.calcular_Nuevo_Valor import calcular_Nuevo_Valor
from Errores.errorR import errorR
from Operaciones.reduccion_polinomio import reduccion_polinomio

class tabla_muller:

    def tabla_muller(self):
        
        instance_evaluar = evaluar()
        instance_calcularC = calcular_Nuevo_Valor()
        instance_errorR = errorR()
        instance_reduccion = reduccion_polinomio()
        flag = True 
        x = sp.symbols('x')
        function = sp.sympify(x**4 - 13*x**2 + 36)
        x0 = 0
        x1 = 1
        x2=2
        
        while(True):   
        
         fx0 =  instance_evaluar.evaluar_muller(x0,0,function)
         fx1 = instance_evaluar.evaluar_muller(x1,0,function)
         fx2 = instance_evaluar.evaluar_muller(x2,0,function)
         h0 = instance_calcularC.calcular_h(x1,x0)
         h1 = instance_calcularC.calcular_h(x2,x1)
         s0 = instance_calcularC.calcular_s(fx1,fx0,h0)
         s1 = instance_calcularC.calcular_s(fx2, fx1,h1)
         a= instance_calcularC.variable_a(s1,s0, h1,h0)
         b= instance_calcularC.variable_b(a,h1,s1)
         c = fx2
         x3 = instance_calcularC.variable_x3(x2,c,b,a)
         error = instance_errorR.errorR(x3,x2)
         print(" x0    |    x1    |    x2    |    f(x0)   |     f(x1)   |     f(x2)   |     h0    |     h1   |     s0    |     s1    |     a    |     b    |    c    |  x3  |Error relativo    ")
         print("{}     |     {}     |      {}     |     {}     |     {}     |    {}     |     {}     |     {}     |     {}     |     {}     |    {}   |    {}    |    {}   |   {}    |     {}   % | ".format
                 (x0, x1, x2,fx0 ,fx1, fx2 , h0, h1,s0, s1,a,b,c,x3, error))
           
         x0 = x1
         x1= x2 
         x2=x3
         if fx0==0 or fx1==0 or fx2==0:
           print("Se requiere una reducciion de polinomio")
           function = instance_reduccion.reduccion_Coeficientes(function,2)
           x0 = 0
           x1 = 1
           x2=2
          
           
           
        
           if error <= instance_errorR.error_Tolerable:
               print("fin ")
               break
        
           


