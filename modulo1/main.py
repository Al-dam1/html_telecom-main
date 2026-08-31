import geometria as geo 
import formato 
# geometria.pi

texto = input('Ingresa tu texto: ')

print('capitalize', formato.capitalize(texto))
print('mayuscula ', formato.mayusculas(texto))
print('minusculas ', formato.minusculas(texto))

print(f"area de circulo: {geo.area_circulo(5)}")

print(f"valor de pi: {geo.pi}")
