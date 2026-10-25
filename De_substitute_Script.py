passphrase = open("passwd.txt", "r").read()
plaintext = open("substitute_proprietary.txt", "r").read()

mapped_pass = ""
j = 0
for i in range(len(plaintext)):
    #maps passphrase to non whitespace chars in text
    if plaintext[i].isalpha() and plaintext[i].islower():
        mapped_pass += passphrase[j].lower()
        j = (j + 1) % len(passphrase)
    elif plaintext[i].isalpha() and plaintext[i].isupper():
        mapped_pass += passphrase[j].upper()
        j = (j + 1) % len(passphrase)
    else:
        mapped_pass += plaintext[i]

decrypted_text = ""
for i in range(len(plaintext)):
    #if char is not int or a whitespace then decrypts with the passphrase
    if plaintext[i].isalpha() and plaintext[i].islower():
        decrypted_text += chr(((ord(plaintext[i]) - ord(mapped_pass[i]))%26) + 97)
    elif plaintext[i].isalpha() and plaintext[i].isupper():
        decrypted_text += chr(((ord(plaintext[i]) - ord(mapped_pass[i]))%26) + 65)


    else:
        decrypted_text += plaintext[i]

print(decrypted_text)
