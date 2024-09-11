import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def menu():
    print("Selecciona una opción:")
    print("1. Sumar 2 números")
    print("2. Restar 2 números")
    print("3. Multiplicar 2 números")
    print("4. Dividir 2 números")
    print("5. Sumar N números")
    print("6. Salir")
    
    return input("Ingresa tu opción: ")

def main():
    while True:
        opcion = menu()
        
        if opcion == '1':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", sumar.sumar(a, b))
        
        elif opcion == '2':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", resta.restar(a, b))
        
        elif opcion == '3':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", multiplicacion.multiplicar(a, b))
        
        elif opcion == '4':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", dividir.dividir(a, b))
        
        elif opcion == '5':
            numeros = input("Ingresa los números separados por espacios: ")
            numeros = list(map(float, numeros.split()))
            print("Resultado:", suma_avanzada.sumar_n(numeros))
        
        elif opcion == '6':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
