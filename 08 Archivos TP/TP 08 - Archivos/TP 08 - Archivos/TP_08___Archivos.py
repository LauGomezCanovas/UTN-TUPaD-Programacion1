#
# TP 08 Manejo de Archivos
# \\

import os
from token import OP

if not os.path.exists("productos.txt"):
    with open("productos.txt", "w") as archivo:
        archivo.write("Lapicera, 120.5, 30\n")
        archivo.write("Lapiz, 100, 20\n")
        archivo.write("Goma, 20, 100\n")

productos = []
def cargar_lista_archivo():

    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split(",")
            nombre = partes[0].strip()
            precio = float(partes[1])
            cantidad = int(float(partes[2]))

            producto = {"nombre": nombre, 
                        "precio": precio, 
                        "cantidad": cantidad}
            productos.append(producto)


def mostrar_productos():
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            # 1) Eliminar espacios y salto de linea
            linea = linea.strip()
        
            # 2) saltar linea vacia o encabezado
            if linea == "" or linea.startswith("nombre"):
                continue

            # 3) separa campos
            lista_productos = linea.split(",")
        
            # 4) quita espacios extra en cada campo con .strip()
            nombre = lista_productos[0].strip()
            precio_str = lista_productos[1].strip()
            cantidad_str = lista_productos[2].strip()

            # 5) convierte a numeros
            precio = float(precio_str)
            cantidad = int(float(cantidad_str))

            # 6) imprime con formato
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

def agregar_producto():
    nombre_nuevo = input("Ingrese el nombre del producto: ")
    precio_nuevo = input("Ingrese el precio: ")
    cantidad_nueva = int(input("Ingrese la cantidad: "))

    precio_nuevo = float(precio_nuevo)
    cantidad_nueva = int(cantidad_nueva)

    productos.append({"nombre": nombre_nuevo, "precio": precio_nuevo, "cantidad": cantidad_nueva})
    
    guardar_en_archivo()



def buscar_producto():
    # 1) Pedir el nombre
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ")

    # 2) Recorrer la lista productos
    for producto in productos:
        # 3) Comparar ignorando mayusculas/minusculas
        if producto["nombre"].lower() == nombre_buscado.lower():
            # 4) Muestra datos
            print(f"Producto encontrado: ")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            return # <- Corta funcion cuando encuentra
    print("El producto ingresado no existe en la lista.")

def guardar_en_archivo():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            nombre = producto["nombre"]
            precio = producto["precio"]
            cantidad = producto["cantidad"]
            archivo.write(f"{nombre}, {precio}, {int(cantidad)}\n")


cargar_lista_archivo()

continuar_operando = True
print("Hola, gracias por ingresar al sistema de revision de Productos.")
while continuar_operando == True:
    continuar_operando = True
    operacion = input("Ingrese la operacion que desea realizar:\n'a'- Para leer el listado de Productos\n'b'- Para agregar un nuevo producto a la lista\n'c'- Para buscar un producto en la lista\n O 's' para salir del sistema\n")
    if operacion.lower() == "a":
        mostrar_productos()
    elif operacion.lower() == "b":
        agregar_producto()
    elif operacion.lower() == "c":
        buscar_producto()
    elif operacion.lower() == "s":
        print("Gracias por usar el sistema de revision de Productos!")
        continuar_operando = False
    else:
        print("El comando ingresado no es valido, Por favor, vuelva a intentarlo")