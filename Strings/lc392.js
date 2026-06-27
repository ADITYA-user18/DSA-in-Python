function PalindromeCounterFromStrin(str){


    let ans=0;
    let odd = false
    if(str.length<=1){
        return str.length
    }

    let d = {}

    for(let i=0;i<str.length;i++){
        if(str[i] in d){
            d[str[i]] +=1
            
        }else{
            d[str[i]] = 1
        }
    }

    

    for(let count of Object.values(d)){
        if(count%2==0){
           ans+=count
        }
        else{
            ans+=count-1
            odd =true

        }
    }

    if(odd){
        ans+=1
    }


    return ans


}

console.log(PalindromeCounterFromStrin('hhhfiufyuqiuwnof'))
