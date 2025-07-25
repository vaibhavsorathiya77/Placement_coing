text = input("Enter text:- ").lower()
if text.isnumeric():
    print("Pls enter valid string")
    exit()

key = int(input("Enter a key:- "))
if key <1 or key >= 26:
    print("Enter between 1 to 25 ")
    exit()

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x',"y",'z']
ct = ""
decry = ""
for i in text:
    if i in alphabets:
        pi = alphabets.index(i)
        ci = int(pi + key) % 26
        ct +=alphabets[ci]
    else:
        ct +=i
print("Encrypted text:- ",ct)

for j in ct:
    if j in alphabets:
        vi = alphabets.index(j)
        dec = (vi - key) % 26
        decry += alphabets[dec]
    else:
        decry += j
print("Decrypted:- ",decry) 
