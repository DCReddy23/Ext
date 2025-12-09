def rail_fence_encrypt(text, key):
    rails = [''] * key
    row, step = 0, 1
    for ch in text:
        rails[row] += ch
        row += step
        if row == 0 or row == key - 1:
            step *= -1
    return ''.join(rails), rails  # ciphertext and rails

def rail_fence_decrypt(rails):
    key = len(rails)
    n = sum(len(r) for r in rails)
    pattern = []
    row, step = 0, 1
    for _ in range(n):
        pattern.append(row)
        row += step
        if row == 0 or row == key - 1:
            step *= -1
    rails = [list(r) for r in rails]
    return ''.join(rails[r].pop(0) for r in pattern)

# Example
cipher, rail_array = rail_fence_encrypt("HELLO WORLD", 3)
print("Encrypted:", cipher)
print("Rails:", rail_array)
print("Decrypted:", rail_fence_decrypt(rail_array))
