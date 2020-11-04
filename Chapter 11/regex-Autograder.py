# Exercise Autograder: 
# The basic outline of this problem is to read the file, look for integers using 
# the re.findall(), looking for a regular expression of '[0-9]+' and then 
# converting the extracted strings to integers and summing up the integers.

import re

fhand = open('regex_sum_1027259.txt')
total = 0

for line in fhand:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    if len(x) > 0:
        for i in x:
            total += int(i)

print(total)
