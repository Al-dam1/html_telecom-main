// Una vivienda del tipo casa a la calle, tiene un fm de 1,07%,
// un departamento en edificio tiene un factor multiplicador de
// 1.04%, una casa en un barrio cerrado tiene un fm de 1.21%,
// y así sucesivamente.

// Podemos definir un costo base de usd 1,16 por metro
// cuadrado de la propiedad. Entonces, si el cliente posee una
// propiedad de 65 m² para asegurar, el costo del seguro será
// la resultante de:
// Costo Base * m² = usd 75,40

metros = prompt('ingresa los metros cuadrados: ')
metros_casa = prompt('tiuene asfalto? ').toLowerCase
metros_edificio = prompt('vive en edificio? ').toLowerCase
metros_quinta = prompt('vive en edificio? ').toLowerCase

costo_base = 1.16
costo_edifico = 1.04
costo_calle = 1.07
costo_quinta = 1.21 

costoTotal = parseInt( metros * costo_base)

if (metros_casa == 'si' && metros_edificio == 'si' && metros_quinta == 'si'):
    costoTotalMas = costoTotal + (costo_calle + costo_edifico + costo_edifico)
    

alert(`el csoto totakl es ${costoTotal}`)