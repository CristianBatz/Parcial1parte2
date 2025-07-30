def calcular_mcd(numeroA,numeroB,residuo,resultado):
    if residuo == 0:
        return 0

def cadena_repetir(cantidad,palabra,i=0):
    if i == cantidad:
        return 0
    else:
        print(f"{palabra}")
        return cadena_repetir(cantidad,palabra,i+1)


opcion = 0
while opcion != 5:
    print("=== Menu recursivo ===")
    print("1. Calcular MCD ")
    print("2. Crear cadena repetida")
    print("3. Cantidad de una letra en una palabra")
    print("4. Conversion decimal a binario")
    print("5. Cantidad de digitos en un numero")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        print("=== Calculando MCD ===")
        numeroA = int(input("Ingrese el primer numero: "))
        numeroB = int(input("Ingrese el segundo numero: "))

    elif opcion == 2:
        print("=== repetir cadena ===")
        palabra = input("Ingrese una palabra: ")
        cantidad = int(input("Ingrese la cantidad que desea repetir: "))
        cadena_repetir(cantidad,palabra)

