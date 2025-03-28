import decrypt
import encrypt

while 1:
    print("1 - Encrypt a file\n2 - Decrypt an encrypted file\n3 - Exit")
    choice = input("Make a selection: ")
    if choice == '1':
        encrypt.enc()
    elif choice == '2':
        decrypt.dec()
    elif choice == '3':
        exit(1)
    else:
        continue
