import sys
import os

# Agregar la carpeta src a sys.path para poder importar desde ella
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar la clase calcularC
from Sistema.Menu import Menu
def main():
    instanciaMenu = Menu()
    instanciaMenu.menu()


if __name__ == "__main__":
    main()
