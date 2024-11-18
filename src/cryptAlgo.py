import os
 
# ASCII conversions
def text_to_ascii(text):
    return [ord(c) for c in text]

def ascii_to_text(ascii_list):
    return ''.join(chr(c) for c in ascii_list)
 
# Random Key
def generate_random_key(length):
    return os.urandom(length)
 
# Encryption and Decryption
def encrypt(plaintext, key):
    plaintext_ascii = text_to_ascii(plaintext)
    encrypted_ascii = [p ^ k for p, k in zip(plaintext_ascii, key)]
 
    # Return encrypted text as hexadecimal string
    encrypted_text_hex = ''.join(f'{num:02x}' for num in encrypted_ascii)
    return encrypted_text_hex
 

def decrypt(ciphertext, key):
    # Convert the hex ciphertext back to ASCII values
    ciphertext_ascii = [int(ciphertext[i:i+2], 16) for i in range(0, len(ciphertext), 2)]
    decrypted_ascii = [c ^ k for c, k in zip(ciphertext_ascii, key)]
 
    # Return the decrypted text
    decrypted_text = ascii_to_text(decrypted_ascii)
    return decrypted_text