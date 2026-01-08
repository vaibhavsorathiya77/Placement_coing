str1 = "listen"
str2= "lisgo"

if (str1.length != str2.length){
    console.log("Not anagram")
}
else{
    let s1 = str1.split("").sort().join("");
    let s2 = str2.split("").sort().join("");
    console.log(s1 === s2)

}