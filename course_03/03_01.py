import re

file = open('regex_sum_2129246.txt')
content = file.read()

numbers = re.findall(r'[0-9]+', content)

total = sum(map(int, numbers))

print("The sum of all numbers is:", total)
