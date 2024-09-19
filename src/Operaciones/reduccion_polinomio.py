import re
import sympy as sp

class reduccion_polinomio: 
    def __init__(self):
        self.flag = False

    def reduccion_Coeficientes(self, funcion, raiz):
        coef = self.coeficientes(funcion)
        coef_reducidos = self.dividir_polinomio(coef, raiz)
        polinomio_resultante = self.convertir_a_funcion(coef_reducidos)
        return str(polinomio_resultante)  # Convertir la expresión a string

    def coeficientes(self, funcion):
        # Convertir el polinomio a una lista de coeficientes
        return [int(coef) for coef in sp.Poly(funcion).all_coeffs()]

    def dividir_polinomio(self, coeficientes, raiz):
        resultado = []
        acumulador = coeficientes[0]
        resultado.append(acumulador)

        for coef in coeficientes[1:]:
            acumulador = acumulador * raiz + coef
            resultado.append(acumulador)

        return resultado[:-1]  # El último valor es el residuo, que debe ser 0

    def convertir_a_funcion(self, coeficientes):
        x = sp.Symbol('x')
        polinomio = 0
        grado = len(coeficientes) - 1
        for i, coef in enumerate(coeficientes):
            polinomio += coef * x**(grado - i)
        return sp.simplify(polinomio)