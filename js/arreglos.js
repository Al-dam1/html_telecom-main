let frutas = ['Manzana', 'Banana','Naranja','Pera','Fresa','Kiwi'];
console.log(frutas)
console.log(frutas[2]); //muestra naranja

//cambia la posicion
frutas.splice(2,0,'Mango');
console.log(frutas[2]);

//necesito arreglar un elemento en mi lista de frutas
// while (frutas.length <8){
//     frutas.push('Frutilla' + (frutas.length + 1)); => FRUTILLA8
// }
while (frutas.length <8){
    frutas.push('Frutilla');
}
console.log(frutas);

//lista de colores
let colores = ['Rojo', 'Verde', 'Azul', 'Amarillo'];

//lista completa
console.log(colores);

//insertar un color en la posicion 1
colores.splice(1,0,'Naranja');
console.log(colores);

// Reemplazar el último color por 'Violeta'
colores[colores.length -1] = 'Violetta';
console.log(colores);

// Usar while para que el arreglo tenga al menos 7 elementos
while (colores.length <7){
    colores.push('Marron');
}
console.log(colores);

// Lista de camionetas
let camionetas = ['Toyota Hilux', 'Ford Ranger', 'Chevrolet S10', 'Nissan Frontier'];
//Mostrar la lista completa en consola.
console.log(camionetas);

//Insertar una camioneta en la posición 2.
camionetas.splice(2,0,'Wolswagen 110')

//Reemplazar la última camioneta por otra marca/modelo.
camionetas[camionetas.length - 1] = 'Fiat Torino';

//Usar while para que la lista tenga al menos 6 elementos, agregando nuevas camionetas.
while (camionetas.length <6){
    camionetas.push('Fiat Uno')
}

//Eliminar el segundo camioneta de la lista.
camionetas.splice(1,1)
//slice = “cortar y copiar” → no toca el original.
//splice = “cortar y pegar” → sí modifica el original.

//Mostrar la lista final.
console.log(camionetas);