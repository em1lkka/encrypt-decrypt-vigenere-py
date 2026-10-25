passphrase = open("passwd.txt", "r").read()
plaintext = open("plain.txt", "r").read()

mapped_pass = ""
j = 0

for i in range(len(plaintext)):
    #maps passphrase to non whitespace chars in text
    if plaintext[i].isalpha() and plaintext[i].islower():
        mapped_pass += passphrase[j].lower()
        j = (j+1)%len(passphrase)
    elif plaintext[i].isalpha() and plaintext[i].isupper():
        mapped_pass += passphrase[j].upper()
        j = (j + 1) % len(passphrase)
    else:
        mapped_pass += plaintext[i]

encrypted_text = ""

for i in range(len(plaintext)):
    #if char is not int or a whitespace then encrypts with the passphrase
    if plaintext[i].isalpha() and plaintext[i].islower():
        encrypted_text += chr((ord(plaintext[i]) -97 + ord(mapped_pass[i])-97)%26 + 97)
    elif plaintext[i].isalpha() and plaintext[i].isupper():
        encrypted_text += chr((ord(plaintext[i]) - 65 + ord(mapped_pass[i]) - 65) % 26 + 65)
    else:
        encrypted_text += plaintext[i]

encrypted_text_file = open("substitute_proprietary.txt", "w").write("".join(encrypted_text))
