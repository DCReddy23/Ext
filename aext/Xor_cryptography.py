s=input("Enter a string to encrypt: ")
encrypted=""
for ch in s:
    new=chr(ord(ch)^ord('A'))
    encrypted+=new
print('Encrypted String:',encrypted)
decrypted=""
for ch in encrypted:
    new=chr(ord(ch)^ord('A'))
    decrypted+=new
print('Decrypted String:',decrypted)
