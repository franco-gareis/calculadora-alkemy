import os


class FileHandler:
    def __init__(self):
        self.history_file = "calculator_history.txt"

    def guardar_resultado(self, mensaje):
        """Guarda el resultado de las ejecuciones de la calculadora."""

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

        print("\nHistorial eliminado correctamente\n")


class Calculadora:
    def __init__(self, primer_numero, segundo_numero):
        self.primer_numero = primer_numero
        self.segundo_numero = segundo_numero
        self.file_handler = FileHandler()

    def ejecutar_operacion(self, opcion):
        """Ejecuta la operacion de la calculadora enviada por el parametro."""

        match opcion:
            case 1:
                self.suma()
            case 2:
                self.resta()
            case 3:
                self.multiplicacion()
            case 4:
                self.division()
            case _:
                print("\nDebe ingresar una opcion valida")

    def _format_message(self, method_name, resultado):
        default_message = "La {} de {} y {} da: {}\n"
        return default_message.format(
            method_name, self.primer_numero,
            self.segundo_numero, resultado
        )

    def suma(self):
        """Suma dos numeros y guarda su resultado"""

        resultado = self.primer_numero + self.segundo_numero
        self.file_handler.guardar_resultado(
            self._format_message(self.suma.__name__, resultado)
        )

    def resta(self):
        """Resta dos numeros y guarda su resultado"""

        resultado = self.primer_numero - self.segundo_numero
        self.file_handler.guardar_resultado(
            self._format_message(self.resta.__name__, resultado)
        )

    def multiplicacion(self):
        """Multiplica dos numeros y guarda su resultado"""

        resultado = self.primer_numero * self.segundo_numero
        self.file_handler.guardar_resultado(
            self._format_message(self.multiplicacion.__name__, resultado)
        )

    def division(self):
        """Divide dos numeros y guarda su resultado"""

        try:
            resultado = self.primer_numero // self.segundo_numero
            self.file_handler.guardar_resultado(
                self._format_message(self.division.__name__, resultado)
            )
        except ZeroDivisionError:
            print("\nNo se puede dividir un numero zero")
