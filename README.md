# numerical-methods
## Metodo Punto raices mltiples
Para crear el metodo raices multiples desarrollamos una clase trabla_raices_multiples:
```python

from Operaciones.evaluar import evaluar
from Operaciones.Calcular.calcularC import calcularC
from Errores.errorR_secante import errorR_secante
class tabla_raices_multiples:
    def tabla_raices_multiples(self):
          #instancias de clases 
        instance_evaluar = evaluar()
        instance_calcularC = calcularC()
        instance_errorR = errorR_secante()
        #variables de valores de tabla ( iniciales )
        x1 = 0
        i = 0
      
        print("i | x1 | f(x1) | f´(x1) | f´´(x1)| x1+1 | Error relativo")
        flag = True 
        while(flag):
         x11 =instance_calcularC.calcular_nuevo_valor_raices_multiples(x1)
         error = instance_errorR.errorR_secante(x11,x1)
       
         
         print("{} | {} | {} | {} |  {} | {} | {}% | ".format(i, x1, instance_evaluar.evaluar_Funcion_raices(x1), instance_evaluar.evaluar_Funcion_raices_derivada(x1,1),instance_evaluar.evaluar_Funcion_raices_derivada(x1,2),x11, error))
         x1 = x11
        
        
         if error <= instance_errorR.error_Tolerable:
               print("fin ")
               break
        
         i=i+1


```
implemente las siguientes para calcuular la derivada y la derivada doble:
```python
    def evaluar_Funcion_raices_derivada(self,a,n):
        x,y = sp.symbols('x y')
        function = x**3 - 5*x**2 + 7*x -3
        d = sp.diff(function,x,n)
        derivada_evaluada = d.subs(x,a)
        return derivada_evaluada
    
    def evaluar_Funcion_raices(self,x):
        return round(x**3 - 5*x**2 + 7*x -3,4)
```


