# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip() # throw away the non-printing characters
    print(line.upper()) # all uppercased
