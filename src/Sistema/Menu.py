
from Sistema.Tabla.tabla_Biseccion  import tabla_Biseccion
from Sistema.Tabla.tabla_Falsa_posicion import tabla_Falsa_posicion
from Sistema.Tabla.tabla_Punto_Fijo import tabla_Punto_Fijo
from Sistema.Tabla.tabla_Secante import tabla_Secante
from Sistema.Tabla.trabla_raices_multiples import tabla_raices_multiples
from Sistema.Tabla.tabla_Neton_Raphson import tabla_Neton_Raphson
from Sistema.Tabla.tabla_muller import tabla_muller
class Menu:
    
    option = 1
    def menu(self):
       isinstance_biseccion =tabla_Biseccion()
       isinstance_Falsa_posicion=tabla_Falsa_posicion()
       instansce_Punto_fijo = tabla_Punto_Fijo()
       instance_Secante = tabla_Secante()
       instance_Raioes_multiples = tabla_raices_multiples()
       instance_ne = tabla_Neton_Raphson()
       instance_muller = tabla_muller()
       flag = True


       while(flag):
        option = int(input("\nBIENVENIDO A MENU PRINCIPAL\nSelecciones el metodo: \n1.Biseccion \n2. Falsa posicion \n3.Punto fijo\n4.Secante \n5. Raices multiples\n6.Newton Raphson \n7. Muller\n"))
        if option == 1 :
            isinstance_biseccion.tabla_de_valores_Biseccion()
        if option == 2:
            isinstance_Falsa_posicion.tabla_de_valores_Falsa_posicion() 
        if option ==3 :
           instansce_Punto_fijo.tabla_Punto_Fijo()
        if option ==4 :
           instance_Secante.tabla_Secante()
        if option == 5:
           instance_Raioes_multiples.tabla_raices_multiples()
        if option == 6:
           instance_ne.tabla_Neton_Raphson()
        if option == 7:
              instance_muller.tabla_muller()
        option = input("deasea continuar(1.si 2.no)")
        if  option != "1":
           flag =False
         
           
           
            
     
           
           
        
           
