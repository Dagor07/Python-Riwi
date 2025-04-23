#QUINTO EJERICIO
#PIDE POR TERMINAL QUE INGRESEN UN NUMERO ENTERO,
#SINO ES ENTERO, ENTONCES IMPRIME UN MENSAJE DE ERROR DICIENDO QUE NO SE ACEPTAN DECIMALES
#ADICIONAL, SI EL NUMERO ES MULTIPLO DE 3, IMPRIME LA PALABRA "FIZZ"
#SI EL NUMERO ES MULTIPLO DE 5, IMPRIME LA PALABRA "BUZZ"
#Y SI ES MULTIPLO DE 15, IMPRIME LA PALABRA "FIZZBUZZ"


# for: Bucle repite algo cuando se sabe la cantidad de repeticiones 

while True: # while: Bucle mientras una condición sea verdadera (no se sabe la cantidad de repeticiones)
    entrada = input("Enter a positive integer (enter 'exit' to finish): ")

    if entrada.lower() == "exit": #.lower convierte el texto a minuscula
        print("End of program")
        break

    if "." in entrada:
        print("ERROR. Decimal numbers are not accepted")
        continue #evita que se ejecute el resto del codigo después de detectar un error, como tratar de convertir un número no válido a int.
# strip borra caracteres al inicio y final.
# lstrip borra caracteres a la izquierda
# rstrip borra caracteres a la derecha
    if not entrada.isdigit(): #Si la entrada NO es un número entero.  
        print("ERROR. Only positive integers are accepted")
        continue
#.isdigit sirve para verificar si todos los caracteres de una cadena son dígitos numéricos (0 al 9)
    number = int(entrada)

    if number < 0:
        print("ERROR. Negative numbers are not accepted")
        continue

    if number % 15 == 0:
        print("FIZZBUZZ")
    elif number % 3 == 0:
        print("FIZZ")
    elif number % 5 == 0:
        print("BUZZ")
    else:
        print("The number is not multiple of 3, 5 or 15")
