#
# TP 09 Recursividad
#

print("Ejercicio 1: ")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Mostrar factoriales desde 1 hasta el numero indicado por el usuario
num = int(input("Ingrese un numero: "))
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

print("Ejercicio 2: ")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Mostrar la serie completa
pos = int(input("Ingrese la posicion maxima: "))
for i in range(pos + 1):
    print(f"F({i}) = {fibonacci(i)}")

print("Ejercicio 3: ")

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Ejemplo
print(potencia(2, 5))  # 32

print("Ejercicio 4: ")

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Ejemplo
numero = int(input("Ingrese un numero decimal: "))
binario = decimal_a_binario(numero)
print(f"Binario: {binario if binario else '0'}")

print("Ejercicio 5: ")

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

# Ejemplo
print(es_palindromo("reconocer"))  # True

print("Ejercicio 6: ")

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

# Ejemplo
print(suma_digitos(1234))  # 10

print("Ejercicio 7: ")

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Ejemplo
print(contar_bloques(4))  # 10

print("Ejercicio 8: ")

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# Ejemplo
print(contar_digito(12233421, 2))  # 3
