
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text,Shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+Shift_key)%26
            cipher_text+=alphabet[new_position]
        else:
            cipher_text += char
    print(f"here is the text after encryption : {cipher_text}")
def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift_key)%26
            plain_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"here is the text after decryption : {plain_text}")
wanna_end=True
while wanna_end:
    what_to_do=input("type 'encrypt' for encryption and 'decrypt' for decryption :   ")
    text=input("type your message here:")
    shift=int(input("Enter your shift key :"))
    if what_to_do == "encrypt":
        encryption(plain_text=text,Shift_key=shift)
    elif what_to_do == "decrypt":
        decryption(cipher_text=text,shift_key=shift)
    want_continue=input("Do you to continue ('yes' or 'no'):")
    if want_continue == "no":
        wanna_end =False

