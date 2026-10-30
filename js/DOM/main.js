const titulo = document.getElementById('titulo');
const parrafo = document.getElementById('parrafo')

console.log(titulo.innerText);
//cambia el titulo
// titulo.innerText = 'Ugarte Carrocerias';

// console.log(parrafo.textContent);
// parrafo.textContent = 'hola hawai'

//innerHTML
const divContenedor = document.getElementById('btn');
console.log(divContenedor.innerHTML);
divContenedor.innerHTML = `<h3>Características del modelo</h3>
                            <p>Diseñado para viajes de larga distancia.</p>
                            <p>Ofrece comodidad para los pasajeros.</p>`

const secion = document.querySelector('.servicios');
console.log(secion.innerHTML); 

// const list = document.getElementsByTagName('li');
// for(let element of list){
//     element.textContent= element.textContent.toUpperCase();
// }

const contenedor = document.getElementById('btn-enviar');

contenedor.onclick = function() {
    contenedor.outerHTML = `
        <div>
            <h1>Gracias por contactarnos</h1>
            <p>Estaremos en contacto.</p>
            <p>Abrazo</p>
        </div>
    `;
};