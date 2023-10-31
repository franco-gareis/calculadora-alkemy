from calculadora import Calculadora

while True:
    try:
        print("""Que operacion desea realizar?\n 1. Suma\n 2. Resta\n 3. Multiplicacion\n 4. Division\n Si desea salir ingrese el numero -1\n""")
        opcion = int(input("Ingrese su opcion: "))
        
        # early return 
        if opcion == -1:
            break
        
        primer_numero = int(input("Ingrese el primer numero: "))
        segundo_numero = int(input("Ingrese el segundo numero: "))
        calc_instance = Calculadora(primer_numero, segundo_numero)
    except ValueError:
        print("Tenes que ingresar un valor que sea un entero.\n")
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
    