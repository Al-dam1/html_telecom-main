const botonAgregar = document.querySelectorAll('.btn-agregar');

for (boton of botonAgregar){
    boton.onclick = function () {
        console.log('Modelo Agregado!');
        
        alert('Modelo Agregado!');
    }
}