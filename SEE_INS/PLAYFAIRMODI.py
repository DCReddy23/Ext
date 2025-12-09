def playfair_simple(text, key, mode="encrypt"):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = "".join(dict.fromkeys(key.upper().replace("J", "I") + alphabet))
    text = text.upper().replace("J", "I").replace(" ", "")
    if mode == "encrypt" and len(text) % 2: 
        text += "X"
    step = 1 if mode == "encrypt" else -1
    result = ""
    for i in range(0, len(text), 2):
        # Get coordinates using divmod (row = index // 5, col = index % 5)
        row_a, col_a = divmod(matrix.index(text[i]), 5)
        row_b, col_b = divmod(matrix.index(text[i+1]), 5)
        if row_a == row_b:   # Same Row
            result += matrix[row_a*5 + (col_a + step) % 5] + matrix[row_b*5 + (col_b + step) % 5]
        elif col_a == col_b: # Same Column
            result += matrix[((row_a + step) % 5)*5 + col_a] + matrix[((row_b + step) % 5)*5 + col_b]
        else:                # Rectangle
            result += matrix[row_a*5 + col_b] + matrix[row_b*5 + col_a]
    return result
key = "MONARCHY"
cipher = playfair_simple("HELLO", key, "encrypt") # Output: CFSU...
plain  = playfair_simple(cipher, key, "decrypt")  # Output: HELLOX
print(f"Encrypted: {cipher}")
print(f"Decrypted: {plain}")