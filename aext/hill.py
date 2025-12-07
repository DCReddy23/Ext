import numpy as np

def hill_encrypt(plain_text, key_matrix):
    plain_text = plain_text.upper().replace(' ', '')
    if len(plain_text) % 2 != 0:
        plain_text += 'X'

    cipher_text = ''
    for i in range(0, len(plain_text), 2):
        pair = [ord(plain_text[i]) - ord('A'), ord(plain_text[i+1]) - ord('A')]
        result = np.dot(key_matrix, pair) % 26
        cipher_text += chr(result[0] + ord('A')) + chr(result[1] + ord('A'))
    return cipher_text

def hill_decrypt(cipher_text, key_matrix):
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    det_inv = pow(det, -1, 26)
    adjugate = np.array([[key_matrix[1][1], -key_matrix[0][1]],
                         [-key_matrix[1][0], key_matrix[0][0]]]) % 26
    inv_key = (det_inv * adjugate) % 26

    plain_text = ''
    for i in range(0, len(cipher_text), 2):
        pair = [ord(cipher_text[i]) - ord('A'), ord(cipher_text[i+1]) - ord('A')]
        result = np.dot(inv_key, pair) % 26
        plain_text += chr(int(result[0]) + ord('A')) + chr(int(result[1]) + ord('A'))
    return plain_text

# Example Usage
key_matrix = np.array([[3, 3], [2, 5]])  # Should be invertible mod 26
plain_text = "HELLO"
cipher_text = hill_encrypt(plain_text, key_matrix)
print("Encrypted:", cipher_text)
print("Decrypted:", hill_decrypt(cipher_text, key_matrix))
