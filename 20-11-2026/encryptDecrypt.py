# Python Encrypt / Decrypt Program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()

random.shuffle(key)

# print(chars)
# print(key)

original_message = input("Enter the message you want to Encrypt: ")
encrypted_message = ""

for letter in original_message:
    index = chars.index(letter)
    encrypted_message += key[index]

print(encrypted_message)

encrypted_message = input("Enter the message you want to Decrypt: ")

original_message = ""

for letter in encrypted_message:
    index = key.index(letter)
    original_message += chars[index]

print(original_message)