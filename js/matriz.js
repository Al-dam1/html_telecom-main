let matriz = [
    ['argentina',2,3],
    ['brasil',5,6],
    ['chile',8,9]
];
console.table(matriz);
//mostrar las posiciones 0 y 4 de la matriz
console.log('posicion 0:', matriz[0][0]);
console.log('posicion 4:', matriz[1][0]);

let numeros = [
    ['', ,''],
    ['', ,''],
    ['', ,''],
    ['', ,''],
    ['', ,''],
    ];

//llenar la matriz con numeros del 1 al 15
let contador = 1;
for (let i = 0; i < numeros.length; i++){
    for(let j = 0; j < numeros[i].length;j++){
        numeros[i][j] = contador;
        contador++
    }
}
console.log('matriz llena:');
console.table(numeros);
//console.log('posicion 4:', numeros[1][2]);
//console.log('posicion 4:', numeros[2][1]);

//necesito recorrer una matriz de 4x4 y mostrar por consola los elemntos
//de la posicion 5 y 0 de cada fila
let evg = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
];

for (let i=0; i < evg.length; i++){
    console.log(`fila ${i} en decreciente:`);
    for (let j = evg[i].length -1; j >=0; j--){
        console.log(evg[i] [j]);
    }
}
