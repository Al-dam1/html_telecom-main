# Ejercicio 1: Variables
# 1. Arma una frase con las 3 variables dadas y
# muéstrala por pantalla.
# Es obligatorio usar las 3 variables, pero también
# puedes agregar palabras para generar una frase.
# No importa el orden que elijas para las variables.
# texto_uno = "potente"
# texto_dos = "sol"
# texto_tres = "triunfo"

texto_uno = "potente"
texto_dos = "sol"
texto_tres = "triunfo"
mensaje = f"El {texto_dos} es poderoso cuando esta {texto_uno} y eso demuestra su {texto_tres} sobre la oscuridad!!"
print(mensaje)

# 2. Realiza un programa que tenga 2 variables,
# base = 10 y altura = 5. Calcula el área de un
# rectángulo y muestra el resultado por
# pantalla.

base = 10
altura = 5
area_de_un_rectangulo = base * altura
mensaje = f"El area del rectangulo es: {area_de_un_rectangulo}"
print(mensaje)

# 3. Dadas 2 variables: a = 20 y b = 10, muestra
# por pantalla su suma, resta, multiplicación y
# división.
a = 20
b = 10
sum = a + b
res = a - b
multi = a * b
divi = a / b
mensaje = f"El resultado de la suma es:{sum},de la resta es:{res}, de la multiplicacion es:{multi} y de la division es:{divi}!!"
print(mensaje)


# Ejercicio 2: Sumar 3 variables
# 1. En un script de Python, crea:
# ● 3 variables nombradas a, b y c con valores
# numéricos cualesquiera.
# ● 1 variable llamada resultado, que sea la
# suma de las primeras tres.
# Imprime en pantalla cada una de ellas. Antes de
# mostrar el valor de cada variable, indica su
# nombre en una línea anterior.
# Este es un ejemplo de lo que se debería mostrar
# en pantalla:
# a:
# 5
# b:
# 7
# c:
# 10
# resultado:
# 22
a = 200
b = 470
c = 820
resultado = a + b + c
print(resultado)

# Ejercicio 3: Cadenas
# ● Crea 2 variables, saludo y nombre, cuyos
# contenidos sean "Hola, " en el primer caso y tu
# nombre en el segundo. Intenta sumarlas con el
# operador +.
# ● Muestra el resultado en pantalla.
# ● Para guardar el resultado de la suma, puedes
# crear una tercera variable.
# A continuación, encontrarás la resolución a los ejercicios
# para que puedas verificar cómo te fue.


saludo = "Hola buenos dias como estas,"
name = "Damian"
recado = saludo + name
print(recado)

# Crea un programa que solicite el nombre de un alumno a
# través de la consola y la cantidad de cursos, y luego
# muestre por pantalla esa información.

alumno = input("Ingresa tu nombre: ")
curso = input("Ingresa la cantidad de cursos incripto: ")
incripto = f"Hola {alumno}, estas incripto en total de {curso} cursos."
print(incripto)

# DESAFIOS!!

# Ejercicio 1
# 1. Resuelve el siguiente problema utilizando las
# herramientas aprendidas en el módulo.
# Tomás rindió 3 exámenes y desea saber su
# promedio a partir de esta información:

nota_uno = 10
nota_dos = 6
nota_tres = 8
suma = nota_uno + nota_dos + nota_tres
total_de_notas = 3
total = suma / total_de_notas
total_promedio = f"El total del promedio de tomas es {total}."
print(total_promedio)

# 2
# Calcule los minutos que hay en una semana declarando variables.
minutos_hora = 60
numero_semanas = 1
cantidad_semna = 7
hora_dia = 24
minutos_semana = minutos_hora * hora_dia * cantidad_semna * numero_semanas
print(minutos_semana)

# Dada una situacion ;
peso_payaso = 112
peso_muñeca = 75
usuario_pasayo = int(input("Indica la cantidad de payasos comprados: "))
usuario_muñeca = int(input("Indica la cantidad de muñecas comprados: "))
calculo_paya= usuario_pasayo * peso_payaso
calculo_muñe= usuario_muñeca * peso_muñeca
total= f"EL PESO TOTAL DE LOS PAYASOS COMPRADOS ES: {calculo_paya}, Y DE LAS MUÑECAS ES: {calculo_muñe} "
print(total)
nombre_curso = "Python Telecom"

descripcion_curso="""
Este curso se dicta por Telecom Argentina ,
para hombres/mujeres que quieren 
involucrse en el mundo IT!!
"""
print(nombre_curso, descripcion_curso)
print(len(descripcion_curso))
print(len(nombre_curso))
print(nombre_curso[:])
print(nombre_curso[7:])
print(nombre_curso[:6])
nombre = "Damian Nicolas"
apellido = "Alderete"
nombre_completo = f"Tu es {nombre}  y tu apellido es {apellido}"
print(nombre_completo)
print(nombre.upper()) #mayuscula
print(nombre.lower()) #minuscula 
print(nombre.capitalize()) #Damian  , primer caracter en MAYUSCULA
print(nombre.title()) #Titulo Python
#metodo strip , saca los espacios q hay en la Izquierda y Derecha.
#encadenar metodos ; print(nombre.strip().capitalize())
