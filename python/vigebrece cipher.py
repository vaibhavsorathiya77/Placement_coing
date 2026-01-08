# Polyalphabetic Cipher (User Input, Simple Version)

# take user input
text = input("Enter the text: ").lower()
key = input("Enter the key: ").lower()

# make key same length as text
key_full = ""
for i in range(len(text)):
    key_full += key[i % len(key)]

table = []
for i in range(26):
    row = ""
    for j in range(26):
        row += chr((i + j) % 26 + ord('A')) + " "
    table.append(row.strip())

print("\n--- Vigenère Table ---\n")
for r in table:
    print(r)


# encryption
encrypted = ""
for i in range(len(text)):
    if text[i].isalpha():
        shift = ord(key_full[i].upper()) - ord('A')
        if text[i].islower():
            encrypted += chr((ord(text[i]) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A'))
    else:
        encrypted += text[i]

print("Encrypted Text:", encrypted)

# decryption
decrypted = ""
for i in range(len(encrypted)):
    if encrypted[i].isalpha():
        shift = ord(key_full[i].upper()) - ord('A')
        if encrypted[i].islower():
            decrypted += chr((ord(encrypted[i]) - ord('a') - shift + 26) % 26 + ord('a'))
        else:
            decrypted += chr((ord(encrypted[i]) - ord('A') - shift + 26) % 26 + ord('A'))
    else:
        decrypted += encrypted[i]

print("Decrypted Text:", decrypted)
