let str = "vaibhav"
rev = ""
for (let i = str.length-1; i>=0; i--){
    rev+=str[i]
}
if (rev===str){
    console.log("Palindrome",rev,str)
}
else{
    console.log("Not an Palindrome",rev,str)
}