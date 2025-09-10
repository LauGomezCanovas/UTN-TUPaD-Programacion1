
# Programa 1:

print("Programa 1")

lista_cien = list(range(4, 101, 4))

print(lista_cien)

# Programa 2:

print("Programa 2")

lista_cinco = [1, 2, 3, 4, 5]

print(lista_cinco[3])

# Programa 3:

print("Programa 3")

lista_vacia = []
lista_vacia.append("Hola")
lista_vacia.append("A")
lista_vacia.append("Todos")

print(lista_vacia)

# Programa 4:

print("Programa 4")

animales = ["perro" , "gato" , "conejo" , "pez"]
animales[1] = "loro"
animales[3] = "oso"

print(animales)

# Ejercicio 5:

print("Programa 5:")
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

print(f"El programa crea una lista llamada numeros y procede a eliminar el valor maximo de la lista")
print(f"El valor maximo de la lista es 22. Despues, imprime la lista, la cual tiene el numero 22 o valor maximo eliminado.")

# Programa 6:

print("Programa 6")

lista_treinta = list(range(10, 31, 5))

print(lista_treinta[0:2])

# Programa 7:

print("Programa 7")

autos = ["sedan" , "polo" , "suran" , "gol"]
autos[1] = "ferrari"
autos[2] = "tesla"
print(autos)

# Programa 8:

print("Programa 8")

dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

# Programa 9:

print("Programa 9")

compras = [["pan" , "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

# Programa 10:

print("Programa 10")

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
