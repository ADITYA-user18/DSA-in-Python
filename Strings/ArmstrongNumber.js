let n  = 153


let original = n


let total = 0
let len = String(n).length

while(n>0){
    let last_digit = n%10

    total += last_digit**len


    n= Math.floor(n/10)

}

if(total==original){
        console.log('Yes arm number')
    }

else{
    console.log('Not arm number')

}
