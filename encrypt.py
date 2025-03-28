print("Please enter a filename.\nInput example: test.txt")

while 1:
    filename = input("Enter filename: ")
    if ("." not in filename) or (" " in filename):
        print("Error: Invalid Input")
    else:
        try:
            file = open(filename, "r")
            break
        except:
            print("Error: Cannot open file")
    break
        
#find the file extension in filename
perIndex = filename.rfind('.')
#replace it with .dec, which our decryption will read
newname = filename[:perIndex] +'.dec'

savefile = open(newname, "w")

for i in file:
    savefile.write((chr(ord(i) * 2)))

