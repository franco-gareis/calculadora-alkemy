class Calculadora:
    
    def __init__(self, primer_numero, segundo_numero):
        self.primer_numero = primer_numero
        self.segundo_numero = segundo_numero
        
    def guardar_historial(self, mensaje):
        with open("history.txt", 'a') as fh:
            fh.writelines(mensaje)

    def sumar(self):
        """Suma dos numeros y retorna su resultado"""
        resultado = f"{self.primer_numero + self.segundo_numero}"
        mensaje = f"La suma de {self.primer_numero} y {self.segundo_numero} es igual a: {resultado}\n"
        self.guardar_historial(mensaje)
        print(mensaje)
    
    def restar(self):
        """Resta dos numeros y retorna su resultado"""
        resultado = f"{self.primer_numero - self.segundo_numero}"
        mensaje = f"La resta de {self.primer_numero} y {self.segundo_numero} es igual a: {resultado}\n"
        self.guardar_historial(mensaje)
        print(mensaje)
    
    def multiplicar(self):
        """Multiplica dos numeros y retorna su resultado"""
        resultado = f"{self.primer_numero * self.segundo_numero}"
        mensaje = f"La multiplicacion de {self.primer_numero} y {self.segundo_numero} es igual a: {resultado}\n"
        self.guardar_historial(mensaje)
        print(mensaje)
    
    def dividir(self):
        """Divide dos numeros y retorna su resultado"""
        try:
            resultado = f"{self.primer_numero // self.segundo_numero}"
            mensaje = f"La division de {self.primer_numero} y {self.segundo_numero} es igual a: {resultado}\n"
            self.guardar_historial(mensaje)
            print(mensaje)
        except ZeroDivisionError:
            print("\nNo se puede dividir un numero zero")
            