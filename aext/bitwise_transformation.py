def transform(s):
    res = ""
    for ch in s:
        x = ord(ch) & 127        # Step 1: limit to 7-bit ASCII
        y = x ^ 127              # Step 2: flip bits using XOR
        z = (y % 95) + 32        # Step 3: ensure printable char (32–126)
        res += chr(z)
    return res

s = input("Enter the string to encrypt: ")

print("Actual String:", s)
encrypted = transform(s)
print("Encrypted:", encrypted)
decrypted = transform(encrypted)
print("Decrypted:", decrypted)
