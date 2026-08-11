n1=input("Ingrese un numero: ")
n2=input("Ingrese segundo numero: ")
n1 = int(n1)
n2 = int(n2)
multi= n1*n2
suma= n1+ n2
divi=n1/n2
resta=n1-n2


resultado_operaciones= f"""
Para los numeros {n1} y {n2},
El resultado de la operacion Suma es:{suma},
El resultado de la multiplicacion es:{multi},
El de la resta:{resta},
y el de division:{divi}"""
print(resultado_operaciones)

print(2=="2")
print(2==2)

#operadores
edad = 12
if edad >18:
    print("Puedes ver la pelicula")
else:
    print("No puedes ver la pelicula porque eres menor!!")
    print("Ve a otro lado!")
print("listo")

edad=90
if edad >70:
    print("tienes un super descuento ")
elif edad >65:
    print("tienes un descuento del 15%")
elif edad >50:
    print("tienes un descuento del 10%")
elif edad >17:
    print("puedes ver la pelicula")

edad = 10
mensaje= "es mayor" if edad >17 else "es menor"
print(mensaje)

#operadores
gas= True
edad= 19
if edad >17 and gas:
    print("puedes avanzar")