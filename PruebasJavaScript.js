var gerson = {
    nombre: 'Gerson',
    apellido: 'Pac',
    edad: 18,
    peso: 75,
    ingeniero: false,
    cantante: false,
    estudiante: true,
    ciclista: false,
    programador: true
}
var mario = {
    nombre: 'Mario',
    apellido: 'Bros',
    edad: '21',
    ingeniero: true,
    cantante: true,
    estudiante: false,
    ciclista: false,
    programador: false
}
const MAYORIADEEDAD = 18

function imprimirProfesiones(persona){
    console.log(`${persona.nombre} es:`);
    if (persona.ingeniero){
        console.log('Ingeniero');
    }

    if (persona.cantante){
        console.log('Cantante');
    }
    if (persona.ciclista){
        console.log('Ciclista');
    }
    if (persona.programador){
        console.log('Programador');
    }
    if (persona.estudiante){
        console.log('Estudiante');
    }
    
}
imprimirProfesiones(gerson)

const mayor = ({edad}) => edad >= MAYORIADEEDAD
// function esMayorDeEdad(persona){
//     return persona >= MAYORIADEEDAD
// }

function mayorDeEdad(persona){

    if (mayor(persona)) {
        console.log(`${persona.nombre} es mayor de edad!`);
        
    } else {
        console.log(`${persona.nombre} es menor de edad!`);
    }
}

console.log(`Al inicio del ano ${gerson.nombre} pesaba ${gerson.peso} kg`);
const INCREMENTO_PESO = 0.2
const DIAS_DEL_ANO = 365

const bajarDePeso = (persona) => persona.peso -= INCREMENTO_PESO
const aumentarDePeso = (persona) => persona.peso += INCREMENTO_PESO
for (var i = 1; i <= DIAS_DEL_ANO; i++){
    var random = Math.random()
    if (random < 0.25){
        aumentarDePeso(gerson)
    }else if(random< 0.5){
        bajarDePeso(gerson)
    }
}

console.log(`Al Fin del ano ${gerson.nombre} pesa ${gerson.peso.toFixed(1)} kg`);

