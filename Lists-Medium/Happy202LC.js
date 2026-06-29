let n = 19
let seen = new Set()

function Multiplier(n,seen){

    if(n==1){
        return true
    }

    if(seen.has(n)){
        return false
    }
    else{
        seen.add(n)
    }

    let string = String(n)
    let list = string.split("")
    for(let i = 0;i<list.length;i++){
        list[i] = Number(list[i])
    }
    let total=0
    for(let i = 0;i<list.length;i++){
        total+=list[i]**2

    }

    return Multiplier(total,seen)




}

console.log(Multiplier(n,seen))
