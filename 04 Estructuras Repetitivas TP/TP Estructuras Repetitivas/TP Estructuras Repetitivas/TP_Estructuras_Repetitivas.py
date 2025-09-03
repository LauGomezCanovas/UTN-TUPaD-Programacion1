# TP ESTRUCTURAS REPETITIVAS

import random

# Programa 1: Imprime todos los numeros enteros desde 0 a 100 (incluyendo ambos) en orden creciente, mostrando un num por linea
#

print("Programa 1: ")

num = 0
for num in range(0 , 101 , 1):
    print(num)

# Programa 2: Solicita al usuario un numero entero y determina la cantidad de digitos de contiene
#

print("Programa 2: ")

num = int(input("Ingrese un numero entero: "))
digit_ammount = 0
while num > 0:
        num = num // 10
        digit_ammount += 1

print(f"La cantidad de digitos es: ", digit_ammount)

# Programa 3: Suma todos los numeros enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores
#

print("Programa 3: ")

numone = int(input("Ingrese el primer numero: "))
numtwo = int(input("Ingrese el segundo numero: "))

if numone > numtwo:
    numone, numtwo = numtwo, numone

suma = 0

for i in range(numone + 1, numtwo):
    suma += i

print(f"La suma de los enteros entre {numone} y {numtwo} es: {suma}")

# Programa 4: Permite al usuario ingresar numeros enteros y los suma en secuencia.
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

print("Programa 4: ")

suma = 0
num = int(input("Ingrese un numero entero (0 para terminar el programa): "))

while num != 0:
    suma += num
    num = int(input("Ingrese otro numero entero (Ingrese 0 para terminar el programa): "))

print("La suma total es: ", suma)

# Programa 5: Juego en el que el usuario tiene que adivinar un numero aleatorio entre 0 y 9. Al final,
# el programa debe mostrar cuantos intentos fueron necesarios para acertar.

print("Programa 5: ")

num = random.randint(0, 9)
guessed_num = int(input("Ingrese un numero entre 0 y 9: "))
attempts = 1

while num != guessed_num:
    guessed_num = int(input("Intente otra vez! Ingrese un numero entre 0 y 9: "))
    attempts += 1

print(f"Adivinaste! el numero es: {num}")
print(f"Te tomo {attempts} intentos.")

# Programa 6: Imprime en pantalla todos los numeros pares comprendidos entre 0 y 100, en orden decreciente.
#

print("Programa 6: ")

num = 100
for num in range(100 , -1 , -2):
    print(num)


# Programa 7: Calcula la suma de todos los numeros comprendidos entre 0 y un numero entero positivo indicado por el usuario
#

print("Programa 7: ")

positive_num = int(input("Ingrese un numero entero positivo: "))

suma = 0

for i in range(0 + 1, positive_num):
    suma += i

print(f"La suma de los enteros entre 0 y {positive_num} es: {suma}")


# Programa 8: Permite al usuario ingresar 100 numeros enteros. Indica cuantos son pares, cuantos impares, cuantos son negativos y cuantos positivos.
#

print("Programa 8: ")

N = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(N):
    num = int(input(f"Ingresa el numero {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Resultados:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# Programa 9: Permite al usuario ingresar 100 numeros enteros y luego calcula la media de esos valores.
#

print("Programa 9: ")

N = 100

suma = 0

for i in range(N):
    num = int(input(f"Ingrese el numero {i+1}: "))
    suma += num

media = suma / N

print("Resultados: ")
print(f"La suma total es: {suma}")
print(f"La media de los {N} numeros ingresados es: {media}")

# Programa 10: Invierte el orden de los digitos de un numero ingresado por el usuario.
# Ejemplo: Si el usuario ingresa 547, el programa debe mostrar 745.

print("Programa 10: ")

num = int(input("Ingrese un numero: "))
inverted = 0

while num > 0:
    digito = num % 10
    inverted = inverted * 10 + digito
    num = num // 10

print("Numero invertido", inverted)