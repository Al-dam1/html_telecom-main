"""# Para poder realizar este laboratorio,
# se recomienda:
# ● Revisar contenidos previos.
# Ejercicio 1
# 3. Pedir la edad por teclado y comparar si es
# mayor o menor de edad. No olvidar de que
# para poder comparar el ingreso, debe ser
# convertido a int, ya que el usuario ingresa un
# número entero.

edad=int(input("ingresa tu edad: "))
if edad > 17:
    print("Eres mayor")
else :
    print("eres menor de edad. no podes ingresar!")


# 1. Crea un programa que permita ingresar dos
# cadenas vía la consola y las compare. Luego,
# debe imprimir un mensaje en caso de que
# sean iguales y otro en caso de que sean
# diferentes.
dato1= str(input("Ingrese un mensaje: "))
dato2= str(input("Ingrese un segundo mensaje: "))
if dato1 != dato2 :
    print("Los datos ingresados son DIFERENTES!!!")
else :
    print("Los datos ingresados son IGUALES!. GRACIAS POR PARTICIPAR!!")

# 2. Crea un programa que solicite el nombre de
# un alumno a través de la consola, y luego
# chequee que no esté vacío. En caso de estarlo,
# tiene que imprimir un mensaje de error; caso
# contrario, deberá imprimir un mensaje
# indicando que se ingresó correctamente.


nombre_alumno= str(input("Ingrese su nombre: "))
if nombre_alumno == "" :
    print("Error: Haz ingresa mal los valores. Intenta de nuevo!!!")
else:
    print(f"Tu nombre es: {nombre_alumno} ")

# Ejercicio 2

# 1. Con un bucle while, incrementar una
# variable entera de uno en uno (desde 0 a 10
# sin incluir). Mostrar por pantalla el resultado
# por vuelta.
numero = 0
while numero < 10:
    print(f"{numero}")
    numero= numero + 1



# 2. Pedir por teclado el nombre de usuario. Si
# está vacío, volver a pedirlo hasta que ingrese
# un nombre. Luego, saludar al usuario. HACERLO CON WHILE!!
nombre_usuario= str(input("Ingrese tu Nombre: "))
if nombre_usuario == "":
    print("Error! intenta de nuevo!!")
    nombre_usuario = input("Ingrese el nombre nuevamente: ")

print(f" HOLA tu nombre es  {nombre_usuario}")"""

# CREAMOS UN CODIGO Q ENTRA EL MONTO DE COMPRA Y VERIFICA SI ES CLIENTE, Y SI POSEE DESCUENTO , SI LO TIENE TENDRA DESCUENTO EXTRAS!!
""" total_compra = float(input("Ingrese el total de la compra: "))
es_cliente = input("Es cliente nuestro? (si/no)").lower()
posee_descuento = input("posee un cupo de descuento? (si/no)").lower()

descuento_cliente = 0
cupon_descuento = 0
if es_cliente == "si":
    descuento_cliente = 0.15
    print("Usted tiene un descuento del 15%")
 elif posee_descuento == "si":
    cupon_descuento = 0.35
    print("Tenes un cupon de descuento del 35%")
    
else:
    print("Usted no es cliente y no pose descuento!") """

# Ejercicio 3

# Se tiene la siguiente lista de nombres:
# 1. Inserta entre Alejandro y Roberto a Paula, y luego
# agrega al final a Silvina.
# 2. Para finalizar, recorre la lista y muestra a todos los
# nombres por pantalla.
# nombres = ["Susana","Alejandro","Roberto"]
# Se tiene una lista de nombres:
# 1. Recorre la lista con un bucle for.
# Ejercicio 4
# nombres = ["Agustina","Marisa","Juan","Osvaldo"]
# 1. Crea un programa que solicite una fila y una
# columna e imprima en pantalla el número en
# esa posición según la siguiente matriz:
# Un ejemplo de entrada y salida es el siguiente
# (los caracteres en azul son ingresados por el
# usuario):
# Ejercicio 5
# matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
# Fila: 1
# Columna: 2
# 6.4
# El resultado es 6.4 porque es el valor ubicado en
# matriz[1][2].
# El programa debe chequear que la fila y la
# columna tengan valores válidos. En este caso, las
# únicas filas válidas son 0 y 1; las columnas, 0, 1 y
# 2. Si alguno de los dos valores es inválido, debe
# mostrar un mensaje de error.
# Ejercicio 6
# 1. Realiza un programa que, ingresando la edad de
# una persona, determine si es menor, mayor con
# edad laboral o jubilado (contemplando jubilado
# para ambos sexos a los 65 años).
# 2. Se tiene la matriz
# Recórrela con 2 sentencias for para mostrar cada uno
# de los elementos que la componen.
# m = [ [10,50,5], [20,30,70], [15,45,80] ]
# Una agencia de viajes tiene un sistema de información
# para paquetes turísticos. Realiza un programa que, al
# ingresar el paquete (solo la letra), genere una
# descripción de lo que contiene cada “combo”.
# Ejercicio 7
# Paquete A Cancún 7 noches + aéreos: u$s 1200 por persona.
# Paquete B Miami 8 noches + aéreos + alquiler de auto: u$s 1500 por persona.
# Paquete C Bariloche 10 noches + aéreos + excursiones: u$s 1300 por persona.
# Paquete D Río de Janeiro 10 noches + aéreos + excursiones: u$s 1400 por persona.
# A continuación, encontrarás la resolución a los ejercicios
# para que puedas verificar cómo te fue.

numero = 0
while numero <=10:
    print(numero)
    numero +=1


