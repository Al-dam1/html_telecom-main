//     📌 Cuándo usar cada uno
//while → cuando la repetición depende de una condición que no sabés cuántas veces se cumplirá.
let i = 0;
while (i <= 5) {
    console.log('numero:', i);
    i++;
}
//Funciona: repite mientras la condición sea verdadera (i <= 5).

//Uso típico: cuando no sabés cuántas veces se va a repetir exactamente, pero depende de una condición que puede cambiar.

//Ejemplo real: leer datos hasta que el usuario escriba "salir", o esperar que un valor llegue a cierto límite.

//for → cuando tenés un número fijo de repeticiones o querés recorrer un rango definido.
for (let i = 1; i <= 10; i++) {
    console.log(i);
}
//Funciona: repite un número de veces definido, con inicio, condición y actualización en una sola línea.

//Uso típico: cuando sabés de antemano cuántas veces querés repetir.

//Ejemplo real: recorrer un array de 10 elementos, imprimir números del 1 al 10.

//acumulador → cuando necesitás ir sumando o procesando datos en cada vuelta.
let suma = 0;
for (let i = 1; i <= 100; i++) {
    suma += i;
}
console.log('suma del 1 al 100:', suma);

//Funciona: acumula valores en cada iteración.

//Uso típico: cálculos repetitivos, como sumar todos los elementos de una lista, calcular promedios, etc.

//Ejemplo real: sumar ingresos de cada mes en un flujo de caja.