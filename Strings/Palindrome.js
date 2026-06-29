let n = 121

let length =  String(n).length

let original =  n

let i  = 0

let rev=0;

while(n>0){
    let last_digit =  n%10
    rev =  rev*10+last_digit;
    n = Math.floor(n/10)


}



if (rev==original){
    console.log('palindrome')
}else{
    console.log('Not a Palindrome')
}
