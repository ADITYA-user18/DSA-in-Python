let n = 9999446516841684

function Djbaje(n){
    if(n<10){
        return n
    }

    let str = String(n)
    let list =  str.split('')
    let total = 0
    for(let i=0;i<list.length;i++){
        list[i]=Number(list[i])
    }

    for(let i=0;i<list.length;i++){
        total+=list[i]
    }

    return Djbaje(total)
}

console.log(Djbaje(n))
