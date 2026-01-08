// // largest of three numbers
// n1 = 1
// n2 = 22
// n3 = 4

// if (n1>=n2){
//     if(n1>=n3){
//         console.log(n1)
//     }else{
//         console.log(n3)
//     }
// }else{
//     if (n2>=n3){
//         console.log(n2)
//     }else{
//         console.log(n3)
//     }
// }

arr = [1,2,45,12,0,122]
largest = arr[0]

for (let i = 1; i<arr.length; i++){
    if (arr[i]>largest){
        largest = arr[i]
    }
}
console.log(largest)