function RemoveDuplicates(str){

    let result = [];

    for(let i = 0;i<str.length;i++){
        let currentLetter = str[i];
        let lastAddedletter = result[result.length-1];

        if(currentLetter==lastAddedletter){
            result.pop()
        }else{
            result.push(currentLetter)
        }

    }

    return result.join('')

}


console.log(RemoveDuplicates('abbaca'))
