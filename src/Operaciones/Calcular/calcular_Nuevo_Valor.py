
import sympy as sp
from math import sqrt
from re import match
from Operaciones.evaluar import evaluar
class calcular_Nuevo_Valor:
    
    # calcular c en metodo biseccion, falsa posicion
    def calcular_Biseccion(self,a ,b ):
            return (a+b)/2
    
    def calcular_Falsa_Posicion(self, a, b):

     instancia_evaluar = evaluar()  
     return (((a * instancia_evaluar.evaluar_Funcion(b)) - (b * instancia_evaluar.evaluar_Funcion(a))) / (instancia_evaluar.evaluar_Funcion(b) - instancia_evaluar.evaluar_Funcion(a)))

    def calcular_nuevo_valor(self,x1,x11,fx11,fx1):
      return  ( x11-fx11*((x11-(x1))/(fx11-(fx1))))
    
    def calcular_nuevo_valor_raices_multiples(self,x1):
     isinstancia_evaluar = evaluar()
     return x1-(( isinstancia_evaluar.evaluar_Funcion_raices_derivada(x1,0)*isinstancia_evaluar.evaluar_Funcion_raices_derivada(x1,1))/(((isinstancia_evaluar.evaluar_Funcion_raices_derivada(x1,1))**2)-(  isinstancia_evaluar.evaluar_Funcion_raices_derivada(x1,0)*isinstancia_evaluar.evaluar_Funcion_raices_derivada(x1,2)  )))
   
   
    
    def calcular_nuevo_valor_nw(self,x1):
       isinstancia_evaluar = evaluar()
       return x1-(isinstancia_evaluar.evaluar_nw_derivada(x1,0)/isinstancia_evaluar.evaluar_nw_derivada(x1,1))
    
    def calcular_h(self, x,y):
       #Es el mismo metodo para h0 y h1 solo cambia las variables 
       return x-y
    
    def calcular_s(self,fx,fy,h):
       return (fx- fy)/h
    
    def variable_a(self,si,s0,h1,h0):
       return (si-s0)/(h1+h0)
    
    def variable_b(self, a, h1,si):
       return (a*h1)+si
    
    
    def variable_x3(self,x2,c,b,a,):
         # Calcula el discriminante
         discriminante = sp.sqrt(b**2 - 4*a*c)
    
    # Calcula las dos posibles soluciones para la raíz cuadrática
         v1 = x2 + (-2*c + discriminante) / (2*a)
         v2 = x2 + (-2*c - discriminante) / (2*a)
    
    # Devuelve la raíz más cercana a cero (si es necesario)
         if abs(v1) < abs(v2):
          return v1
         else:
          return v2

      
       

    
