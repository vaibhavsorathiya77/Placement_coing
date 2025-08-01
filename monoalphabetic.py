alpha = 'abcdefghijklmnopqrstuvwxyz'
key='zyxwvutsrqponmlkjihgfedcba'
pt = "vaibhav"
data={}
for i,j in zip(alpha,key):
        data[i]=j
for i in pt:
    print(data[i],end="")
