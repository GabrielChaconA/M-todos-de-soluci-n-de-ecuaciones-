class errorR_PuntoFijo:
    error_Tolerable = 0.005
    def errorR_PuntoFijo(self, x1,x2):
        return abs(100*((x2-x1)/x2))



