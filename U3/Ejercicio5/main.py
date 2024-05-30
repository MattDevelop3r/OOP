from menuOpciones import menu
from classColeccion import Coleccion

if __name__ == '__main__':

    coleccion = Coleccion()

    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            elemento = input("\nIngresa el elemento a insertar: ")
            posicion = int(input("Ingresa la posición donde insertar el elemento: "))
            try:
                coleccion.insertarElemento(elemento, posicion)
                print("\nElemento insertado correctamente.")
            except ValueError as e:
                print(e)

        elif opcion == 2:
            elemento = input("\nIngresa el elemento a agregar: ")
            coleccion.agregarElemento(elemento)
            print("\nElemento agregado al final de la colección.")

        elif opcion == 3:
            posicion = int(input("\nIngresa la posición del elemento a mostrar: "))
            try:
                coleccion.mostrarElemento(posicion - 1)
            except IndexError as e:
                print(e)
            except:
                print('\nError de otro tipo')
        else:
            print("\nOpción no válida. Por favor, elige una opción entre 1 y 3 (4 para salir).")
        
        opcion = menu()