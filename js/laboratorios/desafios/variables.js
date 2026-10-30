

// 2) En este nuevo archivo JS, definimos los arrays 'datosPropiedad' y 'datosUbicacion'.
const datosPropiedad = [{tipo: 'Casa', factor: 1.009},
                        {tipo: 'P.H.', factor: 1.005},
                        {tipo: 'Depto. Edificio', factor: 1.002},
                        {tipo: 'Barrio Privado', factor: 1.09},
                        {tipo: 'Oficina', factor: 1.079},
                        {tipo: 'Local Comercial', factor: 1.041},
                        {tipo: 'Depósito Logística', factor: 1.072}]

const datosUbicacion = [{tipo: 'CABA', factor: 1.013},
                        {tipo: 'Tandil', factor: 1.004},
                        {tipo: 'Costa Atlántica', factor: 1.029},
                        {tipo: 'Patagonia', factor: 1.000},]


// 3) El encabezado de variables y constantes se simplifica a lo siguiente:
let fmPropiedad
let fmUbicacion
const costoM2 = 1.16

// y los metros cuadrados solicitados quedan igual que antes.
let metros2 = prompt("Ingresa los metros cuadrados de la vivienda: ")


// 4) Eliminamos la variable 'fm' y la cláusula Switch() del ejercicio anterior, y las suplantamos por los cuadros de diálogo prompt() y una iteración sobre cada array de objetos:

// VIVIENDA 
let tipoVivienda = prompt("Selecciona la vivienda a cotizar: \n" +
                          "('Casa', 'P.H.', 'Dto. Edificio')")

    if (tipoVivienda !== '') {
        for (propiedad of datosPropiedad) {
            if (propiedad.tipo === tipoVivienda) {
                fmPropiedad = propiedad
                break
            }
        }
    }

// UBICACION 
let tipoUbicacion = prompt("Selecciona la ubicación de la vivienda: \n" +
                          "('CABA', 'Tandil', 'Costa Atlántica')")

    if (tipoUbicacion !== '') {
        for (ubicacion of datosUbicacion) {
            if (ubicacion.tipo === tipoUbicacion) {
                fmUbicacion = ubicacion
                break
            }
        }
    } 

// 5) Por último, podemos aplicar un cálculo sobre todos los valores recopilados para recién, luego, hacer la operación aritmética correspondiente.

if (fmPropiedad && fmUbicacion && parseInt(metros2)) {
    let resultado = fmPropiedad.factor * fmUbicacion.factor * metros2 * costoM2
    console.log("Resultado de la Póliza: $ " + resultado)
} else {
    console.warn("Hubo un error en los datos ingresados.")
}