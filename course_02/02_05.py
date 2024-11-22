name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except FileNotFoundError:
    print("File not found:", name)
    exit()

di = dict()

for line in handle :
    line = line.rstrip()
    if not line.startswith('From ') :
        continue
    wds = line.split()
    if len(wds) > 1:  
        email = wds[1]
        username = email.split('@')[0]
        di[username] = di.get(username, 0) + 1

largest = -1
sender = None
for k,v in di.items() :
    if v > largest :
        largest = v
        sender = k

print(sender, largest)
