// Una vivienda del tipo casa a la calle, tiene un fm de 1,07%,
// un departamento en edificio tiene un factor multiplicador de
// 1.04%, una casa en un barrio cerrado tiene un fm de 1.21%,
// y así sucesivamente.

// Podemos definir un costo base de usd 1,16 por metro
// cuadrado de la propiedad. Entonces, si el cliente posee una
// propiedad de 65 m² para asegurar, el costo del seguro será
// la resultante de:
// Costo Base * m² = usd 75,40

// metros = parseInt(prompt('Ingresa los metros cuadrados: '))
// metros_casa = prompt('Tiene asfalto su cuadra? ').toLowerCase()
// metros_edificio = prompt('Vive en edificio? ').toLowerCase()
// metros_quinta = prompt('Vive en barrio privado? ').toLowerCase()

//Tarifas
// costo_base = 1.16
// costo_edifico = 1.04
// costo_calle = 1.07
// costo_quinta = 1.21 
// factura = 0
// //---- 
// costoTotal = metros * costo_base

// // && || logica
// if (metros_casa == 'si' ){
//     factura=  costo_calle  * costoTotal
// }
// else if( metros_edificio == 'si'){
//     factura=  costo_edifico * costoTotal
// }
// else{
//     factura = costo_quinta * costoTotal
// }

// alert('Bienvenidos al sistema de la AFIP ARGENTINA')
// alert(`EL COSTO TOTAL ES   ${factura.toFixed(3)}`)

// ------------
edadUser = parseInt(prompt('Ingresa tu edad: '))
if (edadUser <18){
    alert('no puedes entrar')
}
else{
    alert('bienvenido al club')
}

// -------
// Consigna
// Para este caso te proponemos solicitar un
// usuario y clave.
usuario = 'admin'
clave= 1234
ingresoUsuario = String(prompt('Ingresa el usuario: ')).toLocaleLowerCase()
contraseñaUser = parseInt(prompt('Ingresa la contraseña: '))
if (ingresoUsuario != usuario && contraseñaUser != clave){
    alert('la contraseña y usuario no son correctos')
}
else{
    alert('ingreso exitoso')
}