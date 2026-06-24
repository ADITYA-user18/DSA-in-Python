function Compressor(str){

    let res = '';

    for(let i=1;i<str.length;i+=2){

        
        let number = Number(str[i])

        res+=(str[i-1]).repeat(number)

    }

    

    

    return res
}

console.log(Compressor('a3b2c1'))
