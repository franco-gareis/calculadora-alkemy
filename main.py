from calculadora import Calculadora, mostrar_historial, borrar_historial


def menu():
    "Corre el menu principal de la calculadora."
    
    while True:
        try:
            print("""\nQue operacion desea realizar?\n 1. Suma\n 2. Resta\n 3. Multiplicacion\n 4. Division\n 5. Mostrar historial\n 6. Borrar historial \n 9. Salir""")
            opcion = int(input("Ingrese su opcion: "))
            
            match opcion:
                case 9:
                    # match case para salir de la aplicacion
                    break
                case 5:
                    mostrar_historial()
                    continue
                case 6:
                    borrar_historial()
                    continue
            
            primer_numero = int(input("Ingrese el primer numero: "))
            segundo_numero = int(input("Ingrese el segundo numero: "))
            calc_instance = Calculadora(primer_numero, segundo_numero)
        except ValueError:
            print("\nLa calculadora solamente acepta numeros enteros.\n")
            continue
        
        match opcion:
            case 1:
                calc_instance.sumar()
            case 2:
                calc_instance.restar()
            case 3:
                calc_instance.multiplicar()
            case 4:
                calc_instance.dividir()
            case _:
                print("Debe elegir una opcion correcta.\n")


if __name__ == '__main__':
    menu()
    