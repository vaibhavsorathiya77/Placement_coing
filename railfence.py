text = input("Enter the text:- ")
depth = int(input("Enter the depth:- "))
text = text.replace(" ", "")

rows = [""] * depth
row, step = 0, 1

for ch in text:
    for i in range(depth):
        if i == row:
            rows[i] += ch
        else:
            rows[i] += " "
    if row == 0:
        step = 1
    elif row == depth - 1:
        step = -1
    row += step

for r in rows:
    print(r)

res = "".join([r.replace(" ", "") for r in rows])
print(f"Encrypted text:- {res}")

cipher = res
n = len(cipher)

# 1. Count how many chars go in each row
counts = [0] * depth
row, step = 0, 1
for _ in range(n):
    counts[row] += 1
    if row == 0:
        step = 1
    elif row == depth - 1:
        step = -1
    row += step

# 2. Split cipher into row parts
rows2 = []
index = 0
for c in counts:
    rows2.append(list(cipher[index:index+c]))
    index += c

result = []
pointers = [0] * depth
row, step = 0, 1
for _ in range(n):
    result.append(rows2[row][pointers[row]])
    pointers[row] += 1
    if row == 0:
        step = 1
    elif row == depth - 1:
        step = -1
    row += step

plaintext = "".join(result)
print("Decrypted:", plaintext)
