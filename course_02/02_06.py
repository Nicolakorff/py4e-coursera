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
    if len(wds) > 5:
        time = wds[5]
        hour = time.split(':')[0]
        di[hour] = di.get(hour, 0) + 1

sorted_hours = sorted(di.items())

for hour, count in sorted_hours:
    print(hour, count)
