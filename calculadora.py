import os


class FileHandler:
    def __init__(self):
        self.history_file = "calculator_history.txt"

    def guardar_historial(self, mensaje):
        """Guarda el historial de las ejecuciones de la calculadora."""

        with open(self.history_file, "a") as fh:
            fh.writelines(mensaje)

    def mostrar_historial(self):
        """Muestra el historial de la calculadora."""

        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as fh:
                print("\n" + fh.read())
        else:
            print("\nNo hay datos guardados para mostrar\n")

    def borrar_historial(self):
        """Elimina el historial de la calculadora."""

        if os.path.exists(self.history_file):
            os.remove(self.history_file)

        print("\nHistorial eliminado correctamente")


class Calculadora:
    def __init__(self, primer_numero, segundo_numero):
        self.primer_numero = primer_numero
        self.segundo_numero = segundo_numero
        self.file_handler = FileHandler()

    def sumar(self):
        """Suma dos numeros y retorna su resultado"""

        resultado = f"{self.primer_numero + self.segundo_numero}"
        mensaje = "La suma de {} + {} es igual a: {}\n".format(
            self.primer_numero, self.segundo_numero, resultado
        )
        self.file_handler.guardar_historial(mensaje)

    def restar(self):
        """Resta dos numeros y retorna su resultado"""

        resultado = f"{self.primer_numero - self.segundo_numero}"
        mensaje = "La resta de {} - {} es igual a: {}\n".format(
            self.primer_numero, self.segundo_numero, resultado
        )
        self.file_handler.guardar_historial(mensaje)

    def multiplicar(self):
        """Multiplica dos numeros y retorna su resultado"""

        resultado = f"{self.primer_numero * self.segundo_numero}"
        mensaje = "La multiplicacion de {} * {} es igual a: {}\n".format(
            self.primer_numero, self.segundo_numero, resultado
        )
        self.file_handler.guardar_historial(mensaje)

    def dividir(self):
        """Divide dos numeros y retorna su resultado"""

        try:
            resultado = f"{self.primer_numero // self.segundo_numero}"
            mensaje = "La division de {} / {} es igual a: {}\n".format(
                self.primer_numero, self.segundo_numero, resultado
            )
            self.file_handler.guardar_historial(mensaje)
        except ZeroDivisionError:
            print("\nNo se puede dividir un numero zero")
