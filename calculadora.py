import os

history_file = "calculator_history.txt"


class Calculadora:
    def __init__(self, primer_numero, segundo_numero):
        self.primer_numero = primer_numero
        self.segundo_numero = segundo_numero

    def sumar(self):
        """Suma dos numeros y retorna su resultado"""

        resultado = f"{self.primer_numero + self.segundo_numero}"
        mensaje = f"La suma de {self.primer_numero} + {self.segundo_numero} es igual a: {resultado}\n"
        guardar_historial(mensaje)

    def restar(self):
        """Resta dos numeros y retorna su resultado"""

        resultado = f"{self.primer_numero - self.segundo_numero}"
        mensaje = f"La resta de {self.primer_numero} - {self.segundo_numero} es igual a: {resultado}\n"
        guardar_historial(mensaje)

    def multiplicar(self):
        """Multiplica dos numeros y retorna su resultado"""

        resultado = f"{self.primer_numero * self.segundo_numero}"
        mensaje = f"La multiplicacion de {self.primer_numero} * {self.segundo_numero} es igual a: {resultado}\n"
        guardar_historial(mensaje)

    def dividir(self):
        """Divide dos numeros y retorna su resultado"""

        try:
            resultado = f"{self.primer_numero // self.segundo_numero}"
            mensaje = f"La division de {self.primer_numero} / {self.segundo_numero} es igual a: {resultado}\n"
            guardar_historial(mensaje)
        except ZeroDivisionError:
            print("\nNo se puede dividir un numero zero")


def guardar_historial(mensaje):
    """Guarda el historial de las ejecuciones de la calculadora."""

    with open(history_file, "a") as fh:
        fh.writelines(mensaje)


def mostrar_historial():
    """Muestra el historial de la calculadora."""

    if os.path.exists(history_file):
        with open(history_file, "r") as fh:
            print("\n" + fh.read())
    else:
        print("\nNo hay datos guardados para mostrar\n")


def borrar_historial():
    """Elimina el historial de la calculadora."""

    if os.path.exists(history_file):
        os.remove(history_file)

    print("\nHistorial eliminado correctamente")
