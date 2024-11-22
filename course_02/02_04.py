fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
emails = list()

for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') :
        continue
    wds = line.split()
    if len(wds) > 1 :
        emails.append(wds[1])
        count = count +1

for email in emails :
    print(email)
print("There were", count, "lines in the file with From as the first word")
