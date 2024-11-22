import re
print(sum(int(num) for num in re.findall(r'[0-9]+', open('regex_sum_2129246.txt').read())))
