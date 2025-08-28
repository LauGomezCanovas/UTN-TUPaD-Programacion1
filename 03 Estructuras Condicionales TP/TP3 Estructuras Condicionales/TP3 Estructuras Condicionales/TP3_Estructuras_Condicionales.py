import random
from statistics import mode, median, mean

# Programa 1: Solicita la edad del usuario. Si el usuario es mayor de 18 anios, debera mostrar un mensaje en pantalla que diga "es mayor de edad"
#

edad = int(input("Ingrese su Edad:"))
mayor_edad = 18

if edad >= mayor_edad:
    print(f"Es mayor de edad")
else:
    print(f"Es menor de edad")


# Programa 2: Solicita la nota al usuario. Si la nota es >= 6, muestra por pantalla "Aprobado"; en caso contrario, muestra "Desaprobado"
#

nota = int(input("Ingrese su nota:"))
minimo_aprobacion = 6

if nota >= minimo_aprobacion:
    print(f"Aprobado")
else:
    print(f"Desaprobado")

# Programa 3: Permite ingresar solo numeros pares, si el usuario ingresa un numero par, imprime el msj "Ha ingresado un numero par"
# En caso contrario, imprime "Porfavor, ingrese un numero par"

numero = int(input("Ingrese un numero par: "))

if numero % 2 == 0:
    print(f"Ha ingresado un numero par")
else:
    print(f"Porfavor, ingrese un numero par")

# Programa 4: Solicita al usuario su edad e imprime por pantalla a cual de las sig. Categorias pertenece:
# Ninio/a: < 12 ; Adolescente: >= 12 y < 18 ; Adulto/a Joven: >= 18 y < 30 ; Adulto/a: >= 30

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print(f"Pertenece a: Ninio/a")
elif edad >= 12 and edad < 18:
    print(f"Pertenece a: Adolescente")
elif edad >= 18 and edad < 30:
    print(f"Pertenece a: Adulto/a Joven")
elif edad >= 30:
    print(f"Pertenece a: Adulto")

# Programa 5: Permite introducir contrasenias entre 8 y 14 caracteres (Inclusive). Si el usuario ingresa una contrasenia
# de longitud adecuada, imprimir "Ha ingresado una contrasenia correcta"; en caso contrario, imprimir "Porfavor, ingrese una contrasenia de entre 8 y 14 caracteres"

password = input("Ingrese una contrasenia, debe contener entre 8 y 14 caracteres: ")

if len(password) > 7 and len(password) < 15:
    print("Ha ingresado una contrasenia correcta")
else:
    print("Por favor, ingrese una contrasenia de entre 8 a 14 caracteres")

# Programa 6: Toma la lista numeros_aleatorios , calcula su moda, su mediana y su media y las compara para determinar si hay
#  sesgo positivo, negativo o no hay sesgo. Imprimir el resultado.

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Lista de numeros:", numeros_aleatorios)
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media:.2f}")

if moda < mediana < media:
    print("Distribucion con sesgo positivo a la derecha")
elif moda > mediana > media:
    print("Distribucion con sesgo negativo a la izquierda")
else:
    print("No hay sesgo en la distribucion")

# Programa 7: Solicita una frase/palabra al usuario. Si el string ingresado termina con vocal, aniadir un signo de exclamacion al final
# e imprimir el string resultante; de lo contrario, dejar el string tal cual lo ingreso el usuario e imprimirlo.

frase = input("Ingrese una frase o palabra: ")
ultimo_caracter = frase[-1].lower()

if ultimo_caracter in "aeiou":
    frase += "!"

print(frase)

# Programa 8: Solocita al usuario su nombre y el numero 1, 2 o 3 dependiendo de la opcion que desee:
# 1. Nombre en mayusculas , 2. Nombre en minusculas , 3. Nombre con primer letra mayuscula

nombre = input("Ingrese su nombre: ")
opcion_elegida = int(input("Eliga una opcion entre 1, 2 o 3: "))

if opcion_elegida == 1:
    print(nombre.lower())
elif opcion_elegida == 2:
    print(nombre.upper())
elif opcion_elegida == 3:
    print(nombre.title())
else:
    print("Opcion Invalida")

# Programa 9: Pide al usuario la magnitud de un terremoto, clasifique la magnitud en una de las sig. Categorias segun escala Richter:
# <3 : Muy Leve , >=3 y <4 : "Leve" , >=4 y <5 : "Moderado" , >=5 y <6 : "Fuerte" , >=6 y <7 : "Muy Fuerte" , >=7 : "Extremo"

magnitud = int(input("Ingrese la magnitud de un terremoto: "))

if magnitud < 3:
    print("El sismo es Muy Leve")
elif magnitud >= 3 and magnitud < 4:
    print("El sismo es Leve")
elif magnitud >= 4 and magnitud < 5:
    print("El sismo es Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("El sismo es Fuerte")
elif magnitud >=6 and magnitud < 7:
    print("El sismo es Muy Fuerte")
elif magnitud >= 7:
    print("El sismo es Extremo")

# Programa 10: Pregunte al usuario en cual hemisferio se encuentra, que mes del anio es y que dia es.
# El programa utiliza esa informacion para imprimir por pantalla si el usuario se encuentra en otonio, primavera, verano o invierno.

hemisferio = input("En que hemisferio estas? (N/S): ").strip().upper()
mes = input("En que mes estas?: ").strip().lower()
dia = int(input("Que dia del mes es?: "))

# Convierte mes a un numero (Facilita las comparaciones)
meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}
num_mes = meses.get(mes, 0)

# Determinar la estacion
estacion = ""

if num_mes == 0:
    estacion = "Mes invalido"
else:
    if (num_mes == 12 and dia >= 21) or num_mes in [1, 2] or (num_mes == 3 and dia <= 20):
        estacion = "Invierno" if hemisferio == "N" else "Verano"
    elif (num_mes == 3 and dia >= 21) or num_mes in [4, 5] or (num_mes == 6 and dia <= 20):
        estacion = "Primavera" if hemisferio == "N" else "Otonio"
    elif (num_mes == 6 and dia >= 21) or num_mes in [7, 8] or (num_mes == 9 and dia <= 20):
        estacion = "Verano" if hemisferio == "N" else "Invierno"
    elif (num_mes == 9 and dia >= 21) or num_mes in [10, 11] or (num_mes == 12 and dia <= 20):
        estacion = "Otonio" if hemisferio == "N" else "Primavera"
    else:
        estacion = "Datos fuera de rango"

# Muestra Resultado:
print(f"En el hemisferio {hemisferio}, es {estacion}.")