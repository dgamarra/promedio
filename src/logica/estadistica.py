class Estadistica:
    def __init__(self, datos):
        self.__datos = datos

    def promedio(self):
        if len(self.__datos) > 0:
            return sum(self.__datos)/len(self.__datos)
        else:
            return None

    def desviacion_estandar(self):
        if len(self.__datos) == 0:
            return None
        prom = self.promedio()
        varianza = sum((x - prom) ** 2 for x in self.__datos) / len(self.__datos)
        return varianza ** 0.5
