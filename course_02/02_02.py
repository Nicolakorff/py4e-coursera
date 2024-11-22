# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # print(line)
    count = count +1
    # print(count)
    ipos = line.find(':')
    # print(ipos)
    piece = line[ipos+2:]
# print(piece)
    value = float(piece)
    # print(values)
    total += value
if count > 0:
    average = total / count  # Calcular el promedio
    print("Average spam confidence:", average)
else:
    print("No 'X-DSPAM-Confidence' lines found.")
print("Done")
fh.close()
