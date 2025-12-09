def rail_fence_encrypt(text, key):
    rails, row, step = ['']*key, 0, 1
    for ch in text:
        rails[row] += ch
        row += step
        if row == 0 or row == key-1: step *= -1
    return ''.join(rails)

def rail_fence_decrypt(cipher, key):
    # Step 1: build zigzag pattern
    row, step, pattern = 0, 1, []
    for _ in cipher:
        pattern.append(row)
        row += step
        if row == 0 or row == key-1:
            step *= -1

    # Step 2: split cipher into rails
    rails, idx = [], 0
    for r in range(key):
        count = pattern.count(r)
        rails.append(list(cipher[idx:idx+count]))
        idx += count

    # Step 3: rebuild text
    return ''.join(rails[r].pop(0) for r in pattern)
cipher = rail_fence_encrypt("HELLO WORLD", 3)
print("Encrypted:", cipher)
print("Decrypted:", rail_fence_decrypt(cipher, 3))