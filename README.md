# numerical-methods
## Metodo falsa posición
En esta rama se implementó el metodo de falsa posición, teniendo como unico cambio, calcular "c":
esto se logró con el metodo de alcular_Falsa_Posicion
```python 
 def calcular_Falsa_Posicion(self, a, b):

     instancia_evaluar = evaluar()
     return (((a * instancia_evaluar.evaluar_Funcion(b)) - (b * instancia_evaluar.evaluar_Funcion(a))) / (instancia_evaluar.evaluar_Funcion(b) - instancia_evaluar.evaluar_Funcion(a)))

````