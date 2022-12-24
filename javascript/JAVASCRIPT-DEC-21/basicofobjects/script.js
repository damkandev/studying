// objeto person
// person.name => Leonardo
// person.shirt => white

const person = {
    name: 'Leonardo',
    shirt: 'white',
    funcion: function(){
        console.log(this.name, this.shirt) //this es para referirse al objeto actual
        //se pueden almacenar funciones dentro de un objeto
    }
}

console.log(person.name) // dot notation
console.log(person['shirt']) // bracket notation

// assign object
person.phone = "+12345678910"
console.log(person.phone) // dot notation
console.log(person)

const introducer = (name, shirt) => {
    const person = {
        name: name,
        shirt: shirt
    }
    const intro = `Hi, my name is ${name}, and the color of my shirt is ${shirt}`
    return intro
}

console.log(introducer('Damián', "White"))