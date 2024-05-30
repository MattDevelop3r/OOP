import unittest
class TestNumeros(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1,1.0)
    def test_int_str(self):
        self.assertEqual(1,'1')
if __name__ == '__main__':
    unittest.main()




from claseListaEstadistica import ListaEstadistica
import unittest
class TestValidInputs(unittest.TestCase):
    __listaEstadistica: list
    def setUp(self):
        self.__listaEstadistica = ListaEstadistica([1,2,2,3,3,4])
    def test_media(self):
        self.assertEqual(self.__listaEstadistica.mediaAritmetica(),2.5)
    def test_mediana(self):
        self.assertEqual(self.__listaEstadistica.mediana(), 2.5)
        self.__listaEstadistica.append(4)
        self.assertEqual(self.__listaEstadistica.mediana(), 3)
    def test_moda(self):
        self.assertEqual(self.__listaEstadistica.moda(), [2,3])
        self.__listaEstadistica.remove(2)
        self.assertEqual(self.__listaEstadistica.moda(), [3])
if __name__=='__main__':
    unittest.main()     