let fm 
const costoM2 = 1.16
let metros2 = prompt("Ingresa los metros cuadrados de la vivienda: ")

// El f.m. de la vivienda se vuelve dinámico
let tipoVivienda = prompt("Selecciona la vivienda a cotizar: \n" +
                          "('Casa', 'P.H.', 'Dto. Edificio')")

switch(tipoVivienda) {
    case "Casa":
        fm = 1.009
        break
    case "P.H.":
        fm = 1.005
        break
    case "Dto. Edificio":
        fm = 1.002
        break
    default:
        fm = 1.000
}

//validamos que 'fm' sea mayor a 1.000 y que metros2 sea un número
if (fm > 1.000 && parseInt(metros2)) {
    let resultado = fm * metros2 * costoM2
    console.log("Resultado de la Póliza: $ " + resultado)
} else {
    console.warn("Hubo un error en los datos ingresados.")
}
