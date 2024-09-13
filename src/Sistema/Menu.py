
from Sistema.tabla import tabla
class Menu:
    
    option = 1
    def menu(self):
       isinstance_tabla = tabla()
       option = int(input("\nBIENVENIDO A MENU PRINCIPAL\n Selecciones el metodo: \n1.Biseccion \n2. Falsa posicion \n 3.Punto fijo\n"))
       if option == 1 :
           isinstance_tabla.tabla_de_valores_Biseccion()
       if option == 2:
           isinstance_tabla.tabla_de_valores_Falsa_posicion() 
           
           
        
           
