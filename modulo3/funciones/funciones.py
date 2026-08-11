def saludar():
    print("hola mundo")
saludar()


def sumar(a,b):
    resultado = a + b
    return resultado

total = sumar(4,9)

print(total)

def multiplicar_por_dos(numero):
    return numero * 2
valor= int(input("ingrese un numero: "))
resultado= multiplicar_por_dos(valor)
print("el resultado es:", resultado)

#funcion q retorne una lista de colores 
def lista_colores():
    return ["rojo", "verde", "marron"]
print(lista_colores())

#funcion q devuelva el total de una compra con 15% de dscto si es socio sino no hay descto!
# Precios de productos
manteca = 24
coca_cola = 100

def compra(producto, socio):
    # Normalizo entradas por seguridad
    producto = producto.lower()
    socio = socio.lower()

    if producto == "manteca":
        precio = manteca
    elif producto in ("coca_cola", "coca-cola", "coca cola"):
        precio = coca_cola
    else:
        print("Error: ingrese un producto válido (manteca/coca_cola).")
        return None

    if socio == "si":
        precio *= 0.85  # 15% de descuento

    return precio

# Entradas
cliente = input("Ingrese un producto: manteca/coca_cola: ")
es_socio = input("¿Es socio de la comunidad? si/no: ")

# Uso
total = compra(cliente, es_socio)
if total is not None:
    print(f"Total a pagar: ${total:.2f}")


#ejercicos q hacer 