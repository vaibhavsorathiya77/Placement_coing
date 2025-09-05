import math

def extended_euclidean(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        x1, y1, d = extended_euclidean(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return (x, y, d)
def mod_inverse(e, phi):
    x, y, g = extended_euclidean(e, phi)
    if g != 1:
        raise Exception("No modular inverse exists!")
    else:
        return x % phi
    
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

try:
    p = int(input("Enter p: "))
    if p % 2 ==0:
        exit("p must be prime")
    q = int(input("Enter q: "))
    if q % 2 ==0:
        exit("q must be prime")
    if p == q:
        exit("p and q cannot be the same")

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi:
        if math.gcd(e, phi) == 1:
            break
        e += 1
    if e >= phi:
        exit("No valid e found")
    d = mod_inverse(e, phi)
    print("p =", p, " q =", q)
    print("n =", n)
    print("phi =", phi)
    print("Public key (e, n) =", (e, n))
    print("Private key (d, n) =", (d, n))
    msg = int(input("\nEnter a number message to encrypt (must be < n): "))
    if msg >= n:
        exit("Message must be smaller than n")
    cipher = pow(msg, e, n)
    plain = pow(cipher, d, n)
    print("Original Message:", msg)
    print("Encrypted:", cipher)
    print("Decrypted:", plain)

except ValueError as ve:
    print("Value Error:", ve)
except Exception as ex:
    print("Error:", ex)
