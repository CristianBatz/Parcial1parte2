def calcular_mcd(numeroA, numeroB):
    if numeroB == 0:
        return numeroA
    else:
        print(f"mcd:{numeroA},{numeroB}")
        return calcular_mcd(numeroB, numeroA % numeroB)


def cadena_repetir(cantidad, palabra, i=0):
    if i == cantidad:
        return 0
    else:
        print(f"{palabra}")
        return cadena_repetir(cantidad, palabra, i + 1)


def cantidad_letra(cadena, letra, i=0):
    if i == len(cadena):
        return 0
    else:
        return cadena.count(letra)


def convertir_binario(numeroC):
    if numeroC == 0:
        return ""
    else:
        return convertir_binario(numeroC // 2) + str(numeroC % 2)


def calcular_digitos(numeroD, i=0):
    if i == len(numeroD):
        return i
    else:
        return calcular_digitos(numeroD, i + 1)


opcion = 0
while opcion != 6:
    print("=== Menu recursivo ===")
    print("1. Calcular MCD ")
    print("2. Crear cadena repetida")
    print("3. Cantidad de una letra en una palabra")
    print("4. Conversion decimal a binario")
    print("5. Cantidad de digitos en un numero")
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Opcion no valida")
        continue

    match opcion:
        case 1:
            print("=== Calculando MCD ===")
            try:
                numeroA = int(input("Ingrese el primer numero: "))
            except ValueError:
                print("Opcion no valida")
                continue
            numeroB = int(input("Ingrese el segundo numero: "))
            resultado = calcular_mcd(numeroA, numeroB)
            print(f"resultado: {resultado}")

        case 2:
            print("=== repetir cadena ===")
            palabra = input("Ingrese una palabra: ")
            cantidad = int(input("Ingrese la cantidad que desea repetir: "))
            cadena_repetir(cantidad, palabra)

        case 3:
            print("=== Cantidad de una letra en una palabra ===")
            cadena = input("Ingrese la cadena: ")
            letra = input("Ingrese la letra: ")
            cantidad_de_letra = cantidad_letra(cadena, letra)
            print(f"Resultado: la letra: {letra} aparece {cantidad_de_letra} veces")

        case 4:
            print("=== Conversion decimal a binario ===")
            numeroC = int(input("Ingrese un numero: "))
            numero_binario = convertir_binario(numeroC)
            print(f"Resultao: {numero_binario}")

        case 5:
            print("=== Cantidad de digitos en un numero ===")
            numeroC = input("Ingrese un numero: ")
            cantidad_digito = calcular_digitos(numeroC)
            print(f"Resultado: {cantidad_digito}")

        case 6:
            print("saliendo")
