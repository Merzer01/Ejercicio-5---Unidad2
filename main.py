from classManejador import manejador

def menu(m):
    print("MENU DE OPCIONES")
    print("1- ACTUALIZAR VALOR DEL VEHICULO DE CADA PLAN")
    print("2- VALOR DE CUOTA INFERIOR")
    print("3- VALOR TOTAL A LICITAR")
    print("4- MODIFICAR CANTIDAD DE CUOTAS")
    print("0- Salir")

    while True:
        op = int(input("Ingrese opcion: "))
        if op == 1:
            m.opcion1()
            print("\n")
        elif op == 2:
            m.opcion2()
            print("\n")
        elif op  == 3:
            m.opcion3()
            print("\n")
        elif op == 4:
            m.opcion4()
            print("\n")
        elif op == 0:
            print("Saliendo...")
            break


if __name__ == '__main__':
    m = manejador()
    m.readarchivo()
    menu(m)