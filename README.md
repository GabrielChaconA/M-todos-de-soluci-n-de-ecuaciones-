# numerical-methods
## Metodo Punto fijo
### Antes de empezar con el método se reestructuró los archivos para un mejor entendimiento, eliminando la clase tabla y creando una clase para cada metodo


Para el método fijo se creo la clase tabla_Punto_Fijo con la clase tabla_Punto_Fijo(self):
```python
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

```
se incorporó la clase errorR_PuntoFijo,con su metodo errorR_PuntoFijo(self,x1,x2) para calcular el error relativo, ya que este cambia con respecto a los primeros metodos :
```python
class errorR_PuntoFijo:
    error_Tolerable = 0.005
    def errorR_PuntoFijo(self, x1,x2):
        return abs(100*((x2-x1)/x2))

```
Por último se agregó las funciones del método  fijo que por el fin de este trabajo es la suiguiente funcion:

```python

    def evaluar_Funcion_PF(self, a):
        return ((math.exp(a))-4*a)
    
    def evaluar_Funcion_derivada(self,a):
        return(math.exp(a)*(1/4))

```