import math

# Programa 1:

print("Programa 1")

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# Programa 2:

print("Programa 2")

def saludar_usuario(nombre):
    print("Hola, ", nombre ,"!")

nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

# Programa 3:

print("Programa 3")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} anios y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# Programa 4:

print("Programa 4")

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")

# Programa 5:

print("Programa 5")

def segundos_a_horas(segundos):
    return segundos / 3600
segundos = int(input("Ingrese la cantidad de segundos: "))
print(segundos_a_horas(segundos))

# Programa 6:

print("Programa 6")

def tabla_multiplicar(numero):
    print(f"La tabla de multiplicar de {numero} es: ")
    print(numero * 1)
    print(numero * 2)
    print(numero * 3)
    print(numero * 4)
    print(numero * 5)
    print(numero * 6)
    print(numero * 7)
    print(numero * 8)
    print(numero * 9)
    print(numero * 10)

numero = int(input("Ingrese el numero que desea multiplicar: "))
tabla_multiplicar(numero)

# Programa 7:

print("Programa 7")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    #Evita la division por cero >
    division = a / b if b != 0 else "Indefinida (division por cero)"

    return (suma, resta, multiplicacion, division)

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

resultados = operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"Division: {resultados[3]}")

# Programa 8:

print("Programa 8")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu indice de masa corporal (IMC) es: {imc:.2f}")


# Programa 9:

print("Programa 9")

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("\nIngresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}C equivalen a {fahrenheit:.2f}F")

# Programa 10:

print("Programa 10")

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

num1 = float(input("\nIngresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los tres numeros es: {promedio:.2f}")