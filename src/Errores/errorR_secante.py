class errorR_secante:
    error_Tolerable = 0.005
    def errorR_secante(self, x2,x11):
        return round(abs(((x2-x11)/x2)*100),4)