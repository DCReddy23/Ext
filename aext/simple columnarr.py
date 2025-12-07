import math

def columnar_encrypt(plain_text, key):
    n = len(key)
    rows = math.ceil(len(plain_text) / n)
    
    # 1️⃣ Build empty grid
    grid = [['' for _ in range(n)] for _ in range(rows)]
    
    # 2️⃣ Fill the grid row-wise
    idx = 0
    for r in range(rows):
        for c in range(n):
            if idx < len(plain_text):
                grid[r][c] = plain_text[idx]
                idx += 1
            else:
                grid[r][c] = 'X'   # padding

    # 3️⃣ Read column-wise using key order
    cipher_text = ''
    for col in key:
        col_idx = col - 1
        for r in range(rows):
            cipher_text += grid[r][col_idx]

    return cipher_text



def columnar_decrypt(cipher_text, key):
    n = len(key)
    rows = math.ceil(len(cipher_text) / n)
    
    # 1️⃣ Make empty grid
    grid = [['' for _ in range(n)] for _ in range(rows)]
    
    # 2️⃣ Fill column-wise using key order
    idx = 0
    for col in key:
        col_idx = col - 1
        for r in range(rows):
            grid[r][col_idx] = cipher_text[idx]
            idx += 1

    # 3️⃣ Read row-wise to get plaintext
    plain_text = ''
    for r in range(rows):
        for c in range(n):
            plain_text += grid[r][c]

    return plain_text.rstrip('X')
message = "HELLOTRANSPOSITION"
key = [3, 1, 4, 2]

encrypted_col = columnar_encrypt(message, key)
decrypted_col = columnar_decrypt(encrypted_col, key)

print("Columnar Encrypted:", encrypted_col)
print("Columnar Decrypted:", decrypted_col)
