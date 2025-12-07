import string

def generate_playfair_key_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace('J', 'I')))
    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in key + alphabet:
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def playfair_encrypt(plain_text, key):
    matrix = generate_playfair_key_matrix(key)
    plain_text = plain_text.upper().replace('J', 'I').replace(' ', '')
    
    pairs = []
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        b = plain_text[i+1] if i+1 < len(plain_text) and plain_text[i+1] != a else 'X'
        pairs.append((a, b))
        i += 2 if b != 'X' else 1

    def find_position(c):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == c:
                    return row, col

    result = ""
    for a, b in pairs:
        r1, c1 = find_position(a)
        r2, c2 = find_position(b)
        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

def playfair_decrypt(cipher_text, key):
    matrix = generate_playfair_key_matrix(key)

    def find_position(c):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == c:
                    return row, col

    result = ""
    for i in range(0, len(cipher_text), 2):
        a, b = cipher_text[i], cipher_text[i+1]
        r1, c1 = find_position(a)
        r2, c2 = find_position(b)

        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]

    # Remove padding 'X' if it was added between identical letters or at end
    cleaned_result = ""
    i = 0
    while i < len(result):
        if i + 1 < len(result) and result[i+1] == 'X' and (i+2 >= len(result) or result[i] == result[i+2]):
            cleaned_result += result[i]
            i += 2
        else:
            cleaned_result += result[i]
            i += 1
    return cleaned_result

# Example Usage
plain_text = "HELLO"
key = "MONARCHY"

cipher_text = playfair_encrypt(plain_text, key)
print("Encrypted:", cipher_text)

decrypted_text = playfair_decrypt(cipher_text, key)
print("Decrypted:", decrypted_text)
