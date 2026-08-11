# Consigna
# Crea un programa que solicite el nombre de un alumno a
# través de la consola y la cantidad de cursos, y luego
# muestre por pantalla esa información.

# print('Bienvenido al club motel')
# nombreUsuario = input('Hola ingresa tu nombre: ')
# usuarioCursos = input('ingresa la cantidad de cursos hechos: ')

# print('Hola ' + nombreUsuario + ' estas incripto en ' + usuarioCursos + ' cursos, sigue asi!')

# Una juguetería tiene mucho éxito en la venta de
# dos de sus productos: payasos y muñecas. Suele
# hacer ventas por correo y la empresa de logística
# les cobra por el peso de cada paquete, por lo que
# necesitan calcular el peso de los payasos y
# muñecas que saldrán en cada paquete a
# demanda. Cada payaso pesa 112 g y cada
# muñeca, 75 g.
# Ejercicio 2
# Escribe un programa que:
# ● Solicite al usuario el número de payasos y
# muñecas vendidos en el último pedido.
# ● Calcule el peso total del paquete que será
# enviado.

muñecas =  75
payasos = 112

payasoComprado = int(input('ingresa la cantidad de payasos comprados: '))
muñecasComprado = int(input('ingresa la cantidad de muñecas comprados: '))

payasoTotal = payasoComprado * payasos
muñecaTotal = muñecasComprado * muñecas

precioTotal = payasoTotal + muñecaTotal

print('el total del envio es de ' + str(precioTotal) + '. Esto es en base a los payasos comprados ' + str(payasoComprado) + ' y de muñecas comprados ' + str(muñecasComprado))