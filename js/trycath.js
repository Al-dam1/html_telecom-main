// while (true){
//     try {
//         let edad = -5;
//         if (edad <0){
//             throw new console.error('la edad no puede ser negativa');
//         }
//         console.log('tu edad es ' + edad);
//     } catch (error) {
//         console.log('error:', error.message);
//     }
// } catch(error){
//     console.log('error:', erorr.message);
// }

////////////////////////////////
try {
    let edad = -5;
    if (edad <0){
        throw new Error('la edad no puede ser negativa');
    }
    console.log('tu edad es ' + edad);
} catch (error) {
    console.log('error:', error.message);
} 