function PlusOne(arr){

    for(let i = arr.length-1;i>=0;i--){
        if(arr[i]!=9){
            arr[i]+=1
            return arr
        }
        else{
            arr[i]=0
        }
    }


    return [[1]+arr]

}


console.log(PlusOne([5,9]))
