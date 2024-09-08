class tabla:

 def __init__(self,a,b,c):
    self._a = a
    self._b = b
    self._c = c




def show():
        
        print()
        
        
        return
  
def a(self):
        """Getter para el atributo _a"""
        return self._a

   
def a(self, valor):
        """Setter para el atributo _a"""
        if valor < 0:
            raise ValueError("El valor de a no puede ser negativo.")
        self._a = valor

   
def b(self):
        """Getter para el atributo _b"""
        return self._b

def b(self, valor):
        """Setter para el atributo _b"""
        if valor < 0:
            raise ValueError("El valor de b no puede ser negativo.")
        self._b = valor


def c(self):
        """Getter para el atributo _c"""
        return self._c

