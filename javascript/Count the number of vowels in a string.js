let str = "vaibhav"
let result = str.match(/[aeiou]/gi)

let count=0
if (result!=null){
    count = result.length
}
console.log(count)
