#funciones
def sumar(a,b):
    return  a + b
def resta(a,b):
    return  a - b
def multi(a,b):
    return a * b
def divi(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b
   
#pruebas
print(sumar(3,9))
print(resta(10,4))
print(multi(3,9))
print(int(divi(50,2.2)))

def saludar(nombre):
    return f"hola {nombre}, como estas hoy?"
print(saludar("Damian"))

def edad_perro(humana):
    return humana *7
print(edad_perro(10))

def repetir_palabra( palabra , veces):
    return palabra * veces
print(repetir_palabra("hola ",3))

def es_mayor_edad(edad):
    return edad >=18
print(es_mayor_edad(20))
print(es_mayor_edad(15))

def semana(dias):
    return f"Hoy es el dia {dias} de la semana !"
print(semana("martes"))

def contador_letras(letra):
    return len(letra)
print(contador_letras("expreso villa galicia san jose s.a"))