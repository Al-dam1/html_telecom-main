# sumar(a, b)
# restar(a, b)
# multiplicar(a, b)

def sumar(a,b):
    print(f'La suma de {a} + {b} es: {a + b}')

def resta(a,b):
    print(f'La resta de {a} - {b} es: {a - b}')

def multiplicar(a,b):
    print(f'La multiplicacion de {a} * {b} es: {a * b}')

def par(ingresoUser):
    if (ingresoUser % 2 == 0):
        print(f'El numero {ingresoUser} es par')

def impar(ingresoUser):
    if (ingresoUser % 2 != 0):
        print(f'El numero {ingresoUser} es impar')