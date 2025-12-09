import numpy as np

def hill_cipher(text, key, mode="encrypt"):
    text = text.upper().replace(" ", "")
    if len(text) % 2:  
        text += "X"   # pad odd length

    # Inverse key for decryption
    if mode == "decrypt":
        det = int(round(np.linalg.det(key))) % 26
        inv_det = pow(det, -1, 26)  # modular inverse
        adj = np.round(det * np.linalg.inv(key)).astype(int)  # adjugate matrix
        key = (inv_det * adj) % 26 

    result = ""
    for i in range(0, len(text), 2):
        block = np.array([ord(c) - ord('A') for c in text[i:i+2]])
        enc = key.dot(block) % 26
        result += "".join(chr(x + ord('A')) for x in enc)

    return result

key = np.array([[3, 3], [2, 5]])
cipher = hill_cipher("HELLO", key, "encrypt")
plain  = hill_cipher(cipher, key, "decrypt")

print("Encrypted:", cipher)
print("Decrypted:", plain)