# Encryption with Ceaser Cipher Algorithm
'''
	author: jahnavi puppala
'''

alphabets = 'abcdefghijklmnopqrstuvwxyz'
secret_key = 3
character = input("Please enter your message: ")
for i in range(len(character)):
    if character[i] == ' ':
        print(' ')
    else:
        position = alphabets.find(character[i])
        new_position = (position + secret_key) % 26
        print(alphabets[new_position])