import os

#ASCII Converstion to perform XOR
def text_to_ascii(text):
    return [ord(c) for c in text]

def ascii_to_text(ascii_list):
    return ''.join(chr(c) for c in ascii_list)

#Random Key Generator
def generate_key(length):
    return os.urandom(length)

#Encryption and Decryption
def encrypt(plaintext, key):
    plaintext_ascii = text_to_ascii(plaintext)
    ciphertext = [p ^ k for p, k in zip(plaintext_ascii, key)]
    return ciphertext

def decrypt(ciphertext, key):
    decrypted_ascii = [c ^ k for c, k in zip(ciphertext, key)]
    return ascii_to_text(decrypted_ascii)

if __name__ == "__main__":
    message = "Hello, World"
    
    key = generate_key(len(message))
    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)

    print("Original Message:", message)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)






