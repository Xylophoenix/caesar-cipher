
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")
def decrypt(cipher_text, shift_amount):
    decoded_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            old_position = position - shift_amount
            old_letter = alphabet[old_position]
            decoded_text += old_letter
        else:
            decoded_text += letter
    print(f"The decoded message is {decoded_text}")
from art import logo 
print(logo)
run_again = False
while run_again == False:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == "encode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            shift = shift % 26
            encrypt(plain_text = text, shift_amount = shift)
        elif direction == "decode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            shift = shift % 26
            decrypt(cipher_text = text, shift_amount = shift)
        else:
            print("Invalid input")
        run = input("Do you want to run again? :- ").lower()
        if run == "no":
            run_again = True
        
        
        

