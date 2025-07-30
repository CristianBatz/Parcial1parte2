def calcular_mcd(numeroA,numeroB):
    if numeroB == 0:
        return numeroA
    else:
        return calcular_mcd(numeroB, numeroA%numeroB)

def cadena_repetir(cantidad,palabra,i=0):
    if i == cantidad:
        return 0
    else:
        print(f"{palabra}")
        return cadena_repetir(cantidad,palabra,i+1)

def cantidad_letra(cadena,letra,i=0):
    if i == len(cadena):
        return 0
    else:
        return cadena.count(letra)

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
        resultado = calcular_mcd(numeroA,numeroB)
        print(f"resultado: {resultado}")

    elif opcion == 2:
        print("=== repetir cadena ===")
        palabra = input("Ingrese una palabra: ")
        cantidad = int(input("Ingrese la cantidad que desea repetir: "))
        cadena_repetir(cantidad,palabra)

    elif opcion == 3:
        print("=== Cantidad de una letra en una palabra ===")
        cadena = input("Ingrese la cadena: ")
        letra = input("Ingrese la letra: ")
        cantidad_de_letra = cantidad_letra(cadena,letra)
        print(f"Resultado: la letra: {letra} aparece {cantidad_de_letra} veces")

    elif opcion == 4:
        print("=== Conversion decimal a binario ===")


    elif opcion == 5:
        print("=== Cantidad de digitos en un numero ===")
        numeroC = int(input("Ingrese un numero: "))
