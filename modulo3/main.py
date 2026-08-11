import aritmetica as ari
import geometria as geo
import sumatoria as sumar
import saludo 
import cadenas
import azar

print(saludo.saludo("Damian"))

print(cadenas.mayuscula('hola mundo'))
print(cadenas.minuscula('hola cabron'))
print(cadenas.invertir('hola river plate'))

print(azar.tirar_dado())
print(azar.tirar_moneda())

print("=== Aritmética ===")
print("Suma:", ari.sumar(4, 5))
print("Multiplicación:", ari.multiplicar(3, 7))

print("\n=== Geometría ===") 
print("Área rectángulo:", geo.area_rectangulo(5, 2))
print("Perímetro cuadrado:", geo.perimetro_cuadrado(6))


print("Suma:", ari.sumar(4, 5))
print('sumar')
# main.py
""" import geometria as geo

print(f"Área del círculo r=5: {geo.area_circulo(5)}")
print(f"Valor de PI: {geo.PI}")
 """

import time 

# print(time.asctime())
def temporizador(segundos):
    for i in range(segundos, 0, -1):
        print(f"Tiempo restante: {i} segundos", end="\r")
        time.sleep(1)
    print("¡Tiempo completado!!         ")

temporizador(5)

