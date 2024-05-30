import unittest
from coleccion import Coleccion
from classCalefactorElectrico import CalefactorElectrico
from classCalefactorGas import CalefactorGas

class TestColeccion(unittest.TestCase):
    __coleccion: object
    def setUp(self):
        self.__coleccion = Coleccion()
        print(type(self.__coleccion))
        # Agregar calefactores de prueba a la colección
        calefactor_electrico = CalefactorElectrico("Marca1", "Modelo1", "Pais1", 1000, "contado", 1, "no", 2000)
        calefactor_gas = CalefactorGas("Marca2", "Modelo2", "Pais2", 2000, "cuotas", 2, "si", "123456", 3000)
        self.__coleccion.agregar_calefactor(calefactor_electrico)
        self.__coleccion.agregar_calefactor(calefactor_gas)

    def test_insertar_calefactor(self):
        # Crear un calefactor de prueba para insertar
        calefactor_gas = CalefactorGas("Marca3", "Modelo3", "Pais3", 3000, "contado", 3, "no", "654321", 4000)
        self.__coleccion.insertar_calefactor(calefactor_gas, 1)  # Insertar en la primera posición
        # Verificar que el calefactor se insertó correctamente
        self.assertEqual(self.__coleccion.mostrar_tipo_por_posicion(1), "Calefactor a Gas")

    # Continuar con más métodos de prueba para cada función de la clase Coleccion

if __name__ == '__main__':
    unittest.main()