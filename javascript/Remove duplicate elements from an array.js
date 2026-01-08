arr = [12,12,982,123,0]

let unique = []

for (let i = 0; i<arr.length; i++){
    let isDuplicate = false
for (let j = 0; j<unique.length;j++){
    if (arr[i]===arr[j]){
        isDuplicate=true
        break
    }
}
if (!isDuplicate){
    unique.push(arr[i])
}
}
console.log(unique)