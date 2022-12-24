let frutas = ['🍎', '🍏', '🍌', '🍒']
//              0     1     2      3
console.log(frutas)
frutas.push('🌿')
console.log(frutas)
console.log(frutas.slice(0, 2))
// muestra el array desde 0, hasta 2 (incluye 0, pero excluye 2)
console.log(frutas.indexOf('🍒'))
// muestra la posición que coincida con el parametro dado en cuestión
console.log(frutas.length)
// Muestra la cantidad de elementos en el array