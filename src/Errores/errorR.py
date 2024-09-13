class errorR:

    """ el error actual y anterior se refiere a los valores de C  """
    error_Tolerable = 0.005
    def errorRelativo(self,aActual,aAnterior):
        return abs(100*((aActual-aAnterior)/aActual))
     