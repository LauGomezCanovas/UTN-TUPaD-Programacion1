# Programa 1: Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!".
#

print("Hola Mundo!")

# Programa 2: Programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
#

print("// Programa 2:")
nombre = input("Ingrese su nombre:")
print(f"Hola {nombre} !")

# Programa 3: Programa que pide al usuario su nombre, apellido, edad y lugar de residencia
# Imprime por pantalla una oracion con los datos ingresados

print("// Programa 3:")
nombre = input("Bienvenido, porfavor, ingrese su nombre: ")
apellido = input("Porfavor, ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar_residencia = input("Por ultimo, ingrese su lugar de Residencia: ")

print(f"El usuario es {nombre} {apellido} , tiene {edad} anios y vive en {lugar_residencia}")

# Programa 4: Programa que pide al usuario un radio de un circulo e imprime por pantalla su area y perimetro
#

print("// Programa 4:")

radio = float(input("Ingrese el radio de un circulo"))
pi = 3.14
area = pi * radio **2
perimetro = 2 * pi * radio
print(f"El area del circulo es {area:.2f} y el perimetro es {perimetro:.2f}")

# Programa 5: Programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuantas horas equivale
#

print("// Programa 5:")

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

# Programa 6: Programa que pide al usuario un numero e imprima la tabla de multiplicar de dicho numero.
#

print("// Programa 6:")

numero = int(input("Ingrese un numero: "))
print (f"Tabla de multiplicar de {numero}:")
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")

# Programa 7: Programa que pida al usuario dos numeros enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("// Programa 7:")

primernum = int(input("Ingrese un numero entero distinto de 0: "))
segundonum = int(input("Ingrese otro numero entero distinto de 0: "))

print(f"La suma entre {primernum} y {segundonum} da {primernum + segundonum}")
print(f"La resta entre {primernum} y {segundonum} da {primernum - segundonum}")
print(f"La multiplicacion entre {primernum} y {segundonum} da {primernum * segundonum}")
print(f"La division entre {primernum} y {segundonum} da {primernum / segundonum}")

# Programa 8: Programa que pida al usuario su altura y su peso e imprima por pantalla su indice 
# de masa corporal. 

print("// Programa 8:")

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
IMC = peso / altura**2
print(f"Su indice de masa corporal es {IMC}")

# Programa 9: Programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit. 

print("// Programa 9:")

tempCelsius = float(input("Ingrese una temperatura en grados Celsius: "))
tempFahrenheit = (tempCelsius * 9/5) + 32
print(f"{tempCelsius} C equivalen a {tempFahrenheit:.2f} F")

# Programa 10: Programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos numeros.

print("// Programa 10:")

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres numeros es: {promedio:.2f}")