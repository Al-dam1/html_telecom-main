# Para poder realizar este laboratorio,
# se recomienda:
# ● Revisar contenidos previos.
# Ejercicio 1

# 1. Crea un programa que permita ingresar dos
# cadenas vía la consola y las compare. Luego,
# debe imprimir un mensaje en caso de que
# sean iguales y otro en caso de que sean
# diferentes.
# dato1 = str(input("Ingrese un dato: "))
# dato2 = str(input("Ingrese otro dato: "))
# if dato1 == dato2:
#     print("Los datos son iguales!!!")
# else:
#     print("Los datos son diferentes!!")
# 2. Crea un programa que solicite el nombre de
# un alumno a través de la consola, y luego
# chequee que no esté vacío. En caso de estarlo,
# tiene que imprimir un mensaje de error; caso
# contrario, deberá imprimir un mensaje
# indicando que se ingresó correctamente.
# nombre_alum = str(input("Ingrese el nombre del alumno: "))
# if nombre_alum == "":
#     print("El nombre esta incorrecto!")
# else:
#     print(f"El nombre del alumno es {nombre_alum}!!")
# 3. Pedir la edad por teclado y comparar si es
# mayor o menor de edad. No olvidar de que
# para poder comparar el ingreso, debe ser
# convertido a int, ya que el usuario ingresa un
# número entero.
# solicitar_edad= int(input("Solicito q ingrese su edad por favor: "))
# if solicitar_edad > 17:
#     print("Eres mayor de edad!")
# else:
#     print("Ingreso DENEGADO!. Eres menor de edad!")

# Ejercicio 2

# 1. Con un bucle while, incrementar una
# variable entera de uno en uno (desde 0 a 10
# sin incluir). Mostrar por pantalla el resultado
# por vuelta.
i = 0
while i < 10 :
    print(i)
    i= i+1
    
# 2. Pedir por teclado el nombre de usuario. Si
# está vacío, volver a pedirlo hasta que ingrese
# un nombre. Luego, saludar al usuario.
nombre=str(input("Ingresa el nombre de usuario: "))
while nombre == "":
    print("Error!")
    nombre= input("Ingresa nuevamente el nombre de usuario!")
print("hola " + nombre)
# Ejercicio 3

# Se tiene la siguiente lista de nombres:
# 1. Inserta entre Alejandro y Roberto a Paula, y luego
# agrega al final a Silvina.
lista = [ "susana" ,"Alejandro", "Roberto"]
lista.insert(2, "paula")

indice = 0
while indice < len(lista):
    print(lista[indice])
    indice = indice + 1

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
ingreso_paquete= str(input("Ingrese el del combo: ")).lower()
if ingreso_paquete == "a":
    print("Cancún 7 noches + aéreos: u$s 1200 por persona.")
elif ingreso_paquete == "b":
    print("Miami 8 noches + aéreos + alquiler de auto: u$s 1500 por persona.")
elif ingreso_paquete == "c":
    print("Bariloche 10 noches + aéreos + excursiones: u$s 1300 por persona.")
elif ingreso_paquete == "d":
    print("Río de Janeiro 10 noches + aéreos + excursiones: u$s 1400 por persona.")
else:
    input("ingrese unb combo!: ")
    print("codigo no encontrado") 