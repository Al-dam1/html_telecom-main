# numero = 10
# while numero > 0:
#     print(f"{numero}")
#     numero= numero - 1

# Creá un while que empiece en 0 y llegue hasta 50, mostrando solamente los números múltiplos de 5.
# contador = 0
# while contador <50:
#     contador += 5
#     print(contador)

# bucl for
# se aplican siempre a listas
# alumnos = ['pedro', 'juan','lourdes']

# for alumno in alumnos :
#     print(f'hola {alumno} que tengas lindo dia!')

# Recorré la lista con for y mostrálos uno por uno.
# productos = ['Remera', 'Pantalon', 'Campera', 'Zapatillas']
# for producto in productos:
#     print(producto)

# Usá for para mostrar cada número.

# Después intentá hacer que muestre:

# El número es 10
# El número es 25
# numeros = [10, 25, 8, 40, 15]

# for numero in numeros:
#     print(f'El numero es {numero}')

# 8. Sumar números
total = 0
# numeros = [10, 20, 30, 40, 50]
# Usá un for para sumar todos los números.
# Resultado:
# 150
# for numero in numeros:
#     total = total + numero
# print('resultado: ')
# print(total)
# numeros = [5, 10, 15]
# for numero in numeros:
#     total = total + numero
# print(total) 
# precios = [1000, 2500, 500, 3000]
# for precio in precios:
#     total = total + precio
# print(total)

# numeros = [2, 4, 6, 8, 10]
# for numero in numeros:
#     total = total + numero
# print(total)

#        ---- for if
# numeros = [3, 8, 12, 5, 20, 7, 10]
# for numero in numeros:
#     if (numero > 10):
#         print(numero)
# totalNumero = 0
# numeros = [3, 8, 12, 5, 20, 7, 10, 15]
# for numero in numeros:
#     if (numero %  2 == 0):
#         print(numero)
#         totalNumero = totalNumero + 1
# print(f'hay un total de {totalNumero} numeros')
# totalNumeros = 0
# numeros = [5, 12, 8, 21, 30, 7, 14, 3]
# for numero in numeros:
#     if (numero > 10):
#         print(numero)
#         totalNumeros = totalNumeros + numero
# print(f'la suma de los numeros mayores a 10 son {totalNumeros}')

# -------- while
numero = 1

contador = 0

while numero < 10:

    if numero % 2 == 0:

        print(numero)

        contador = contador + 1

    numero = numero + 1   

print(f'hay {contador} numeros pares')