//muestro los  elementos en la posicion 0 y 4

let frutas = ['naranja','pera','sandia','kiwi','frutilla'];
console.log(frutas);
console.log('elemento en la posicion 0 es ; ' + frutas[0]);
console.log('elemento en la posicion 4 es ; ' + frutas[4]);


//arregar un elelento utulizando FOR
for (let i = 0; i < 5; i++){
    frutas.push('fruta ' + i);
}
console.log(frutas);