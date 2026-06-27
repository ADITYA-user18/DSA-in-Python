

function adi(n){
    if(n<=2){
        return n
    }

    let curr

    let prev1 = 1
    let prev2 = 2

    for(let i=3;i<=n;i++){
        curr = prev1+prev2
        prev1 = prev2
        prev2 = curr
    }

    return curr

}


console.log(adi(5))
