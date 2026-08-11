# VALIDAR SI ES PESO PESADO O PESO PLUMA
pesoPerson = 70

if pesoPerson >70:
    print('ustes es peso pluma')
else:
    print('es peso pesado')


# solisitar q ingrese un color y dependendo del color le digo la prenda 

usuarioColor = str(input('ingresa un color (rosa/negro/marron/azul) : \r\n'))
if usuarioColor == 'rosa':
    print('la prenda es una camisa')
elif usuarioColor == 'negro':
    print('la prenda es una zapatilla')
elif usuarioColor == 'marron':
    print('son unos zapatos')
elif usuarioColor == 'azul':
    print('es una remera deportiva')
else:
    print('ese color no existe en el sistema')