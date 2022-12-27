//medir la frecuencia de una letra en una frase
// ej: haha => ({'a':2},{'h':2})

const letterFre = (frase) => {
    let resultado = []
    
    for(let i = 0; i < frase.length; i++){
        for(let o = 0; o < 4; o++){
            console.log(o)
        }
        /*for(let o = 0; i < frase.length; o++){
            if(frase[i] == frase[o]){
                resultado.push(frase[i], frase[o])
                console.log(resultado)
            }
        }*/
    }
    return (frase.length)
}

console.log(letterFre("haha"))