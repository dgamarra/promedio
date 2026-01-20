import unittest
from src.logica.estadistica import Estadistica


class TestEstadistica(unittest.TestCase):
    def test_promedio_vacio_retornaNone(self):
        datos = Estadistica([])
        self.assertIsNone(datos.promedio())

    def test_promedio_unElemento_retornaValorUnicoElemento(self):
        datos = Estadistica([5])
        self.assertEqual(5, datos.promedio())

    def test_promedio_dosElementos_retornaPromedioElementos(self):
        datos = Estadistica([5, 7])
        self.assertEqual(6, datos.promedio())

    def test_promedio_nElementos_retornaPromedioNElementos(self):
        datos = Estadistica([2, 4, 8, 9, 10, 15])
        self.assertEqual((2+4+8+9+10+15)/6, datos.promedio())

    def test_desviacionEstandar_conjuntoVacio_retornaNone(self):
        datos = Estadistica([])
        self.assertIsNone(datos.desviacion_estandar())

    def test_desviacionEstandar_unElemento_retornaCero(self):
        datos = Estadistica([5])
        self.assertEqual(0, datos.desviacion_estandar())

    def test_desviacionEstandar_nElementos_retornaDesviacionEstandar(self):
        datos = Estadistica([2, 4, 8, 9, 10, 15])
        # Promedio = 8.0
        # Suma de cuadrados de diferencias = (2-8)^2 + (4-8)^2 + (8-8)^2 + (9-8)^2 + (10-8)^2 + (15-8)^2
        # = 36 + 16 + 0 + 1 + 4 + 49 = 106
        # Varianza = 106 / 6 = 17.666...
        # Desviacion = sqrt(17.666...) = 4.20317...
        esperado = (106/6)**0.5
        self.assertAlmostEqual(esperado, datos.desviacion_estandar(), places=5)
