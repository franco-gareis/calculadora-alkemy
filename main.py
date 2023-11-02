from calculadora import Calculadora, FileHandler
from textwrap import dedent


def menu():
    "Corre el menu principal de la calculadora."

    file_handler = FileHandler()

    while True:
        try:
            print(dedent("""\
                \nQue operacion desea realizar?
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
                case _:
                    primer_numero = int(input("Ingrese el primer numero: "))
                    segundo_numero = int(input("Ingrese el segundo numero: "))
                    calculadora = Calculadora(primer_numero, segundo_numero)
                    calculadora.ejecutar_operacion(opcion)
        except ValueError:
            print("\nLa calculadora solamente acepta numeros enteros.")
            continue


if __name__ == '__main__':
    menu()
