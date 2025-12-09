def columnar_encrypt(text, key):
    n = len(key)
    # pad text
    while len(text) % n != 0:
        text += 'X'

    # split into rows
    rows = [text[i:i+n] for i in range(0, len(text), n)]

    # read columns in key order
    return ''.join(row[k-1] for k in key for row in rows)


def columnar_decrypt(cipher, key):
    n = len(key)
    rows = len(cipher) // n

    # prepare empty grid
    grid = [['']*n for _ in range(rows)]
    idx = 0

    # fill columns in key order
    for k in key:
        col = k - 1
        for r in range(rows):
            grid[r][col] = cipher[idx]
            idx += 1

    # read row by row
    return ''.join(''.join(r) for r in grid).rstrip('X')


# Example
msg = "HELLOCOLUMNARTRANSPOSITION"
key = [3, 1, 4, 2]

enc1 = columnar_encrypt(msg, key)
enc2 = columnar_encrypt(enc1, key)
dec1 = columnar_decrypt(enc2, key)
dec2 = columnar_decrypt(dec1, key)

print("Original:", msg)
print("Encrypted Once:", enc1)
print("Encrypted Twice:", enc2)
print("Decrypted Once:", dec1)
print("Decrypted Twice (Recovered):", dec2)
