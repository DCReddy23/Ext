SBOX = [
    0x63, 0x7C, 0x77, 0x7B,
    0xF2, 0x6B, 0x6F, 0xC5,
    0x30, 0x01, 0x67, 0x2B,
    0xFE, 0xD7, 0xAB, 0x76
]

# Inverse S-box
INV_SBOX = [0]*16
for i, v in enumerate(SBOX):
    INV_SBOX[v % 16] = i

# Convert text to 16 bytes
def pad16(s):
    s = s[:16]
    return s + " "*(16 - len(s))

# SubBytes step (simple)
def sub_bytes(block):
    return bytes([SBOX[b % 16] for b in block])

# Inverse SubBytes
def inv_sub_bytes(block):
    return bytes([INV_SBOX[b % 16] for b in block])

# ShiftRows step (simple rotate)
def shift_rows(block):
    b = list(block)
    return bytes([
        b[0], b[5], b[10], b[15],
        b[4], b[9], b[14], b[3],
        b[8], b[13], b[2], b[7],
        b[12], b[1], b[6], b[11]
    ])

# Inverse ShiftRows
def inv_shift_rows(block):
    b = list(block)
    return bytes([
        b[0], b[13], b[10], b[7],
        b[4], b[1], b[14], b[11],
        b[8], b[5], b[2], b[15],
        b[12], b[9], b[6], b[3]
    ])

# AddRoundKey (XOR)
def add_round_key(block, key):
    return bytes([block[i] ^ key[i] for i in range(16)])

# Simple key (16 bytes)
def pad_key(k):
    k = k[:16]
    return k + "0"*(16 - len(k))

# Encryption
def encrypt(plain, key):
    plain = pad16(plain).encode()
    key = pad_key(key).encode()

    block = add_round_key(plain, key)
    block = sub_bytes(block)
    block = shift_rows(block)
    return block

# Decryption
def decrypt(cipher, key):
    key = pad_key(key).encode()
    block = inv_shift_rows(cipher)
    block = inv_sub_bytes(block)
    block = add_round_key(block, key)
    return block.rstrip(b" ").decode()

# MAIN
pt = input("Enter plaintext: ")
key = input("Enter key: ")

ct = encrypt(pt, key)
print("Ciphertext (bytes):", ct)
print("Ciphertext (HEX):", ct.hex())

dt = decrypt(ct, key)
print("Decrypted text:", dt)
