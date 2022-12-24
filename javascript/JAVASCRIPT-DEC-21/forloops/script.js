let fruits = ['🍒', '🍌', '🍏', '🍎', '🍊', '🍉'] // 🍒🍌🍏🍎🍊🍉
for (let i=0; i < fruits.length; i++ ){
    console.log(fruits[i])
}

result = []

for(const fruta of fruits){
    result.push('🍌')
}

console.log(result)