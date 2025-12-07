def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Example Usage
plain_text = "HELLO WORLD"
shift = 3
cipher_text = caesar_encrypt(plain_text, shift)
print("Encrypted:", cipher_text)
print("Decrypted:", caesar_decrypt(cipher_text, shift))
