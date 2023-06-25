import sys

productos = []  

def validar_numero_parte(numero_parte):
    return True

def grabar_producto():
    numero_parte = input("Ingrese el número de parte: ")
    if not validar_numero_parte(numero_parte):
        print("Número de parte inválido.")
        return

    nombre_producto = input("Ingrese el nombre del producto: ")
    if len(nombre_producto) < 6:
        print("Nombre del producto debe tener al menos 6 caracteres.")
        return

    precio_producto = float(input("Ingrese el precio del producto: "))
    if precio_producto <= 0:
        print("Precio del producto debe ser mayor a cero.")
        return

    producto = {
        'numero_parte': numero_parte,
        'nombre_producto': nombre_producto,
        'precio_producto': precio_producto
    }
    productos.append(producto)
    print("Producto grabado exitosamente.")

def buscar_producto():
    numero_parte_buscar = input("Ingrese el número de parte a buscar: ")
    encontrado = False
    for producto in productos:
        if producto['numero_parte'] == numero_parte_buscar:
            encontrado = True
            if producto['precio_producto'] >= 500:
                print("Número de parte:", producto['numero_parte'])
                print("Nombre del producto:", producto['nombre_producto'])
                print("Precio del producto:", producto['precio_producto'])
            else:
                print("Producto sin stock.")
            break
    if not encontrado:
        print("Producto no encontrado.")

def imprimir_reporte():
    for producto in productos:
        print("Nombre del producto:", producto['nombre_producto'])
        print("Número de parte:", producto['numero_parte'])
        print("Descripción del producto: Este es un producto con valor:", producto['precio_producto'])

def salir():
    print("¡Gracias por utilizar el programa!")
    sys.exit()

def mostrar_menu():
    print("==== MENU ====")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir")
    print("4. Salir")

def ejecutar_opcion(opcion):
    if opcion == '1':
        grabar_producto()
    elif opcion == '2':
        buscar_producto()
    elif opcion == '3':
        imprimir_reporte()
    elif opcion == '4':
        salir()
    else:
        print("Opción inválida.")

while True:
    mostrar_menu()
    opcion_elegida = input("Ingrese el número de opción: ")
    ejecutar_opcion(opcion_elegida)

