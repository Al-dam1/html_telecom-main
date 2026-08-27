//para analizar la confiabilidad de una pyme se necesitan q al momento una resolucion de solicitud de cretido la empresa en cuestion muestre el fjujo de caja del ultimo año, el flujo de caja es la descripcion de como varia el dinero a lo largo del tiempo

//si hay mas ingreso q los de ereso significa que significa q se gana., si hay mas egreso q ingreso significa que se pierde dinero., diseña una aplicacion javascript que recibe el fliujo de caja dek utimo año de una empresa y muestre si dicho flujo genera gananci o perdidas.


// Flujo de caja de la empresa (mes, ingreso, egreso)
let flujoCaja = [
    ['enero', 3000, 2000],
    ['febrero', 2800, 3100],
    ['marzo', 3500, 2500],
    ['abril', 4000, 3800],
    ['mayo', 3200, 3300],
    ['junio', 5000, 4200],
    ['julio', 4500, 4600],
    ['agosto', 3800, 3000],
    ['septiembre', 4100, 3900],
    ['octubre', 3700, 4000],
    ['noviembre', 4600, 3500],
    ['diciembre', 6000, 5500],
  ];
  
  let balanceAnual = 0;
  
  for (let i = 0; i < flujoCaja.length; i++) {
    let mes = flujoCaja[i][0];
    let ingreso = flujoCaja[i][1];
    let egreso = flujoCaja[i][2];
    let balanceMensual = ingreso - egreso;
  
    // mostrar situación mensual
    if (balanceMensual > 0) {
      console.log(`${mes}: Ganancia de $${balanceMensual}`);
    } else if (balanceMensual < 0) {
      console.log(`${mes}: Pérdida de $${Math.abs(balanceMensual)}`);
    } else {
      console.log(`${mes}: Equilibrio`);
    }
  
    // acumular en el balance anual
    balanceAnual += balanceMensual;
  }
  
  // mostrar balance anual
  if (balanceAnual > 0) {
    console.log(`Balance anual: GANANCIA de $${balanceAnual}`);
  } else if (balanceAnual < 0) {
    console.log(`Balance anual: PÉRDIDA de $${Math.abs(balanceAnual)}`);
  } else {
    console.log(`Balance anual: EQUILIBRIO`);
  }
  