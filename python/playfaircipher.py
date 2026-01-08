key = input("Enter the key: ").upper().replace("J", "I")
matrix = ""
for c in key:
    if c not in matrix and c.isalpha():
        matrix += c

for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ": 
    if c not in matrix:
        matrix += c

playfair = [list(matrix[i:i+5]) for i in range(0, 25, 5)]

print("\nPlayfair Matrix:")
for row in playfair:
    print(row)

text = input("\nEnter the text: ").upper().replace("J", "I")
prepared = ""
i = 0
while i < len(text):
    a = text[i]
    b = ""
    if i+1 < len(text):
        b = text[i+1]
    else:
        b = "X"

    if a == b:
        prepared += a + "X"
        i += 1
    else:
        prepared += a + b
        i += 2

if len(prepared) % 2 != 0:
    prepared += "X"

print("Prepared Text (in digraphs):", " ".join([prepared[i:i+2] for i in range(0, len(prepared), 2)]))

def find_position(ch):
    for r in range(5):
        for c in range(5):
            if playfair[r][c] == ch:
                return r, c
    return None, None

encrypted = ""
for i in range(0, len(prepared), 2):
    a, b = prepared[i], prepared[i+1]
    r1, c1 = find_position(a)
    r2, c2 = find_position(b)

    if r1 == r2:  # same row
        encrypted += playfair[r1][(c1+1)%5] + playfair[r2][(c2+1)%5]
    elif c1 == c2:  # same column
        encrypted += playfair[(r1+1)%5][c1] + playfair[(r2+1)%5][c2]
    else:  # rectangle
        encrypted += playfair[r1][c2] + playfair[r2][c1]

print("Encrypted Text:", encrypted)

# Step 4: Decryption
decrypted = ""
for i in range(0, len(encrypted), 2):
    a, b = encrypted[i], encrypted[i+1]
    r1, c1 = find_position(a)
    r2, c2 = find_position(b)

    if r1 == r2:  # same row
        decrypted += playfair[r1][(c1-1)%5] + playfair[r2][(c2-1)%5]
    elif c1 == c2:  # same column
        decrypted += playfair[(r1-1)%5][c1] + playfair[(r2-1)%5][c2]
    else:  # rectangle
        decrypted += playfair[r1][c2] + playfair[r2][c1]

print("Decrypted Text:", decrypted)
