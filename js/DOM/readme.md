//// DOM
1. Qué funcionalidades DOM podés agregar


1. Botón para mostrar más información

Por ejemplo, un botón «Conocé nuestros servicios» que despliegue una sección con información sobre reparación, mantenimiento y trabajos de carrocería.
Nivel principiante
Practicás: querySelector, addEventListener, classList.toggle().


2. Filtro de servicios

Mostrás varias tarjetas y agregás botones para filtrar por categoría: «Todos», «Reparación», «Mantenimiento», etc. Al elegir una categoría, se ocultan las tarjetas que no correspondan.
Nivel principiante/intermedio
Practicás: querySelectorAll, forEach, dataset, style.display y condicionales.


3. Formulario para solicitar un presupuesto

El cliente escribe su nombre, teléfono, tipo de vehículo y trabajo que necesita. JavaScript valida los campos y muestra un mensaje personalizado.
Nivel principiante/intermedio
Practicás: value, submit, preventDefault(), if/else y textContent.


4. Galería de trabajos

Al hacer clic en una foto, se abre más grande en una ventana; al tocar la cruz o fuera de ella, se cierra.

Practicás: eventos click, modificar atributos, agregar y quitar clases CSS.



En resumen; el DOM HTML es totalmente
manipulable desde JS, para generar contenido
dinámico, de acuerdo a nuestra necesidad.

● Los archivos scripting de JS que deben
interactuar con el DOM, deben tener el tag
defer y ser referenciados dentro del apartado
<head> de un documento HTML.
Resumen: el DOM HTML desde JavaScript

● El objeto document cuenta con el método
.getElementById() para enlazarnos con un
elemento HTML por su atributo id y,
.querySelector(), para enlazar con un
elemento HTML aprovechando múltiples
posibles combinaciones de selectores.

● Las propiedades .innerText y .textContent,
permiten interactuar con el texto de elementos
HTML desde JS y la propiedad .innerHTML
permite leer y/o generar bloques de código
HTML dinámico.

● Finalmente, .getElementsByTagName() -
.getElementsByClassName() y
.querySelectorAll(), son métodos que nos
permiten enlazar con múltiples elementos
HTML, creando una colección, o array, para
iterarlo y aplicar múltiples modificaciones de
forma simultánea.