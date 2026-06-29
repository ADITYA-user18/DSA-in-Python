n =  9875

function additioner(n){

    if(n<10){
        return n
    }

    let str = String(n)
    let list = str.split('')
    for(let i = 0;i<list.length;i++){
        list[i]=Number(list[i])
    }
    let total = 0
    for(let i = 0;i<list.length;i++){
        total+=list[i]

    }

    return additioner(total)




}

console.log(additioner(n))
