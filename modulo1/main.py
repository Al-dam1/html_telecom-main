import geometria as geo 
import formato 
import notas 
import aritmetica
# geometria.pi

# texto = input('Ingresa tu texto: ')

# print('capitalize', formato.capitalize(texto))
# print('mayuscula ', formato.mayusculas(texto))
# print('minusculas ', formato.minusculas(texto))

# print(f"area de circulo: {geo.area_circulo(5)}")

# print(f"valor de pi: {geo.pi}")

# print('Aca ingresa tu nota y veras la calificacion')

# calificacionUser = int(input('ingresa tu nota: '))

# notas.calificar(calificacionUser)

# aritmetica
aritmeticaUser1 = int(input('ingresa un numero: '))
aritmeticaUser2 = int(input('otro numero: '))

aritmetica.sumar(aritmeticaUser1, aritmeticaUser2)
aritmetica.resta(aritmeticaUser1, aritmeticaUser2)
aritmetica.multiplicar(aritmeticaUser1, aritmeticaUser2)

# Pedí un número.
# Llamá a las dos funciones.
# Mostrá el result

userNumero = int(input('Ingresa un numero: '))
aritmetica.par(userNumero)
aritmetica.impar(userNumero)