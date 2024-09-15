class errorR:
    #aqui se utilizan los valores de la funcion evaluada en c, el actual y anterior
    error_Tolerable = 0.005
    def errorR(self, x2,x11):
        return round(abs(((x2-x11)/x2)*100),4)