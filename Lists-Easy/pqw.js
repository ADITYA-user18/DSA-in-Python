let arr = [16,17,4,3,5,2]

let maxi = 0


let res = []
for(let i = arr.length-1;i>=0;i--){
    if(arr[i]>maxi){
        maxi = arr[i]
        res.push(arr[i])
    }
}


console.log(res)
