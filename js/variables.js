// let numero = prompt('escribe un numero: ');
// if (numero % 2 === 0){
//     console.log(numero + ' es par');
// } else{
//     console.log(numero + ' es impar');
// }

   //📌 Ejercicios con variables
//Variable string  
//Declara una variable con tu nombre y muestra un saludo en consola.
let nombreCompleto = 'damian nicolas alderete';
console.log(`Hola ${nombreCompleto} se bienvenido a la aplicacion en Javascript.`);
//Variable numérica  
//Declara una variable con tu edad y muestra en consola cuántos años tendrás dentro de 10 años.
let años = 23;
let añosFuturo = años + 10;
console.log(`tienes ${años} y en 10 años tendras ${añosFuturo} años.`);
//Variable booleana  
//Declara una variable que indique si sos mayor de edad (true o false) y muéstrala en consola.
let edad_boll = true;
if (edad_boll >= 18){
    console.log('Sos mayor de edad');
}else{
    console.log('sos menor de edad!');
}
//Operaciones matemáticas  
//Declara dos variables numéricas y muestra la suma, resta, multiplicación y división.
const num1 = 20;
const num2 = 49;
let suma = num1 + num2;
let resta =  num1 - num2;
let multi = num1 * num2;
let divi =  parseFloat( num1 / num2);
console.log(`Estas en la aplicacion en javascript numerica y veras suma,resta,multiplicacion y division de los numeros ${num1} y el numero ${num2} `);
console.log(`suma: ${suma}`);
console.log(`resta: ${resta}`);
console.log(`multiplicacion: ${multi}`);
console.log(`division: ${divi}`);

//Concatenación de strings  
//Declara dos variables con palabras y únelas en una sola frase.
let frase1 = 'alfajor';
let frase2 = 'sol serrano';
console.log(`Hay un ${frase1} que es muy rico y es de la marca ${frase2}!!`);
//Interpolación con backticks  
//Usa template literals para mostrar una frase que combine nombre y edad.
console.log(`Hola ${nombreCompleto} tienes ${años} se bienvenido a la aplicacion en Javascript.`);
//Cambio de valor  
//Declara una variable con un número, cámbiale el valor y muestra ambos resultados.
let numer = 100;
console.log(numer);
numer = 23;
console.log(numer);
//Comparación  
//Declara dos variables numéricas y muestra si la primera es mayor que la segunda.
let numerica1 = 20;
let numerica =50;
console.log(numerica1);
console.log(numerica);

if (numerica1 > numerica){
   
    console.log(`numero ${numerica1} es mayor que ${numerica} `);
}else{
    console.log(`numero ${numerica1} es menor a ${numerica}`);
}
//Variable indefinida  
//Declara una variable sin asignarle valor y muestra qué aparece en consola.
let equipo  ;
console.log(equipo);
//Casting de tipos  
//Declara una variable string con un número "25", conviértelo a número y súmale 5.
let strings = '25';
console.log(strings);
numeroConvertido = Number(strings);
console.log(numeroConvertido + 5);