def rail_fence_encrypt(plain_text, key):
    rail = [['\n' for _ in range(len(plain_text))] for _ in range(key)]
    
    dir_down = False
    row, col = 0, 0
    
    for char in plain_text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row += 1 if dir_down else -1

    cipher_text = ''
    for i in range(key):
        for j in range(len(plain_text)):
            if rail[i][j] != '\n':
                cipher_text += rail[i][j]

    return cipher_text


def rail_fence_decrypt(cipher_text, key):
    rail = [['\n' for _ in range(len(cipher_text))] for _ in range(key)]
    
    dir_down = None
    row, col = 0, 0

    # Mark the places with '*'
    for _ in range(len(cipher_text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher_text)):
            if rail[i][j] == '*' and index < len(cipher_text):
                rail[i][j] = cipher_text[index]
                index += 1

    result = ''
    row, col = 0, 0
    for _ in range(len(cipher_text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        result += rail[row][col]
        col += 1
        row += 1 if dir_down else -1

    return result
message = "HELLOTRANSPOSITION"
key = [3, 1, 4, 2]

# Rail Fence
rail_key = 3
encrypted_rail = rail_fence_encrypt(message, rail_key)
decrypted_rail = rail_fence_decrypt(encrypted_rail, rail_key)

print(f"Rail Fence Encrypted: {encrypted_rail}")
print(f"Rail Fence Decrypted: {decrypted_rail}")
