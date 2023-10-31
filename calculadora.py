class Calculadora:
    
    def __init__(self, primer_numero, segundo_numero):
        self.primer_numero = primer_numero
        self.segundo_numero = segundo_numero
        
    def sumar(self):
        """Suma dos numeros y retorna su resultado"""
        print(f"La suma de {self.primer_numero} y {self.segundo_numero} es igual a: {self.primer_numero + self.segundo_numero}\n")
    
    def restar(self):
        """Resta dos numeros y retorna su resultado"""
        print(f"La resta de {self.primer_numero} y {self.segundo_numero} es igual a: {self.primer_numero - self.segundo_numero}\n")
    
    def multiplicar(self):
        """Multiplica dos numeros y retorna su resultado"""
        print(f"La multiplicacion de {self.primer_numero} y {self.segundo_numero} es igual a: {self.primer_numero * self.segundo_numero}\n")
    
    def dividir(self):
        """Divide dos numeros y retorna su resultado"""
        try:
            print(f" La division de {self.primer_numero} y {self.segundo_numero} es igual a: {self.primer_numero // self.segundo_numero}\n")
        except ZeroDivisionError:
            print("No se puede dividir un numero zero")