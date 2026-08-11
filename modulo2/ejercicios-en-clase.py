# EJERCIOS EN CLASE!!!
# Bucle While
"""
secreto = 15
intento = 0
while intento != secreto :
    intento=int(input("Adivina el numero (1-50): "))

    if intento < secreto:
        print("Mas alto es el numero!!")
    elif intento > secreto:
        print("Mas bajo es el numero!!")
print("Correcto! El numero era", secreto)
"""
# Condicionales simples
# VALIDAR SI EL PESO DE LA PERSONA ES MAYOR A 70KG ES PESO PLUMA, SINO ES PESO PESADO.
""" persona=int(input("Ingrese su peso por favor: "))
if persona > 70:
    print("usted es peso pesado")
else :
    print("usted es peso pluma")
 """


# condicionales multiples
# SOLICITAR AL USUARIO QUE INGRESE UN COLOR Y DEPENDIENDO DEL COLOR VA A IMPRIMIR SI ES JEANS,ZAPATILLAS O CAMISA...

""" usuario = input("Ingresa un color (verde/rojo/negro/violeta/marino): ").lower()
if usuario == "verde":
    print("Es una media")
elif usuario == "rojo":
    print("Es una chomba ")
elif usuario == "negro":
    print("Es un pantalon de vestir")
elif usuario == "violeta":
    print("Es una campera")
elif usuario == "marino":
    print("Es una camisa")
else:
    print("Este color no se encontro!!") """

#Bucle While
#solicitar al usuario contraseña y validar la cantidad de intento disponibles y correctos..
contraseña = "unab"  
intento = 3
while intento > 0:
    ingreso = str(input("Ingresa la contraseña: "))   
    if ingreso == contraseña:
        print("Correcto!! La contraseña era", contraseña)
        break
    else:
        intento -=1
        print(f"La contraseña es incorrecta!!.Te queda {intento} intentos por verificar! " )
       
  