def caesar(txt,sht):
    res=''
    for ch in txt:
        if ch.islower():
            res+=chr((ord(ch)-ord('a')+sht)%26+ord('a'))
        else:
            res+=chr((ord(ch)-ord('A')+sht)%26+ord('A'))
    return res

plain  = input()
shift=int(input("enter shift value : "))
enc    = caesar(plain, shift)    # Encrypt with shift = +3
dec    = caesar(enc,  -shift)    # Decrypt by using -35
print("Plain Text :", plain)
print("Encrypted Text :", enc)
print("Decrypted Text :", dec)