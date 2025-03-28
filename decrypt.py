print("Please enter a filename.\nInput example: test.dec")

while 1:
    filename = input("Enter filename: ")
    if (".dec" not in filename) or (" " in filename):
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
#add dec, then save as txt
newname = filename[:perIndex] + '_dec.txt'

savefile = open(newname, "w")

for i in file:
    for j in i:
        savefile.write(chr(ord(j) / 2))

