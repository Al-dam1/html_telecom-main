// let animales = ['Perro', 'Gato', 'Conejo', 'Loro', 'Tortuga'];
// console.log(animales);
// console.log(animales[2]);
// animales.splice(2,0,'hamster');
// console.log(animales[2]);

// while (animales.length <8){
//     animales.push('Animal Nuevo');
// }
// console.log(animales);
// animales.splice(2,2)
// console.table(animales);

// ejercicio 2
// let comida = ['Pizza','Hambuerguesa','Milanesa','Empanada'];
// console.log(comida);
// console.log(comida[2]);
// comida[comida.length -1] = 'Pasta' //remplaza el ultimo por pasta
// console.log(comida);
// while (comida.length <7){
//     comida.push('Tarta');
// };
// console.table(comida);
// comida.splice(3,1);
// console.table(comida);

// ejercicio 3
// let juegos = ['Minecraft', 'FIFA', 'GTA', 'FORNITE', 'ROBLOX'];
// console.log(juegos);
// console.log(juegos[3]);
// juegos.splice(2,0,'MARIO BROS');
// console.log(juegos);
// juegos[juegos.length -1] = 'THE LAST OF US'
// console.log(juegos);

// while (juegos.length <8){
//     juegos.push('SIMNSOMS')
// }
// console.table(juegos);
// juegos.splice(2,1);
// console.table(juegos);

// ejercicio 4
// let productos = ['remera', 'pantalon', 'campera','gorra'];
// console.log(productos);
// console.log(productos[2]);
// productos.splice(0,0,'Buzo');
// productos[productos.length -1] = 'Medias';
// while (productos.length <7){
//     productos.push('Producto nuevo')
// }
// console.log(productos);
// productos.splice(3,1);
// console.log(productos);

// ejercicio 5
let ciudades = ['Buenos Aires', 'Cordoba','Mendoza','Rosario'];
ciudades.splice(1,0,'La Plata');
console.log(ciudades);
ciudades.splice(3,0,'salta');
console.log(ciudades);
ciudades.pop();
console.log(ciudades);
while (ciudades.length <7){
    ciudades.push('Ciudad Nueva')
}
console.log(ciudades);
console.log(ciudades.length);