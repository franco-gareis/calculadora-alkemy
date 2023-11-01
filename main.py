from calculadora import Calculadora, FileHandler
from textwrap import dedent


def menu():
    "Corre el menu principal de la calculadora."

    file_handler = FileHandler()

    while True:
        try:
            print(dedent("""\
                Que operacion desea realizar?
                1. Suma
                2. Resta
                3. Multiplicacion
                4. Division
                5. Mostrar historial
                6. Borrar historial
                9. Salir\n"""))
            opcion = int(input("Ingrese su opcion: "))

            match opcion:
                case 9:
                    # match case para salir de la aplicacion
                    break
                case 5:
                    file_handler.mostrar_historial()
                    continue
                case 6:
                    file_handler.borrar_historial()
                    continue

            primer_numero = int(input("Ingrese el primer numero: "))
            segundo_numero = int(input("Ingrese el segundo numero: "))
            calculadora = Calculadora(primer_numero, segundo_numero)
        except ValueError:
            print("\nLa calculadora solamente acepta numeros enteros.")
            continue

        match opcion:
            case 1:
                calculadora.sumar()
            case 2:
                calculadora.restar()
            case 3:
                calculadora.multiplicar()
            case 4:
                calculadora.dividir()
            case _:
                print("Debe elegir una opcion correcta.\n")


if __name__ == '__main__':
    menu()
