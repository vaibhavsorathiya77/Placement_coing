arr=[12,2,326,912]
small = arr[0]
largest = arr[0]

for (let i = 0; i<arr.length; i++){
    if (arr[i]>largest){
        largest = arr[i]
    }
    if (arr[i]<small){
        small = arr[i]
    }
}
console.log(largest)
console.log(small)