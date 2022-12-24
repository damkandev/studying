const howManyLetters = () => {
    const frase = "hola"

    for (letra in frase){
        console.log(letra)
    }
}

console.log(howManyLetters())