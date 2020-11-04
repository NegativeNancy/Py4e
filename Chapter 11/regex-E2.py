# Exercise 2: 
# Write a program to look for lines of the form:
#
# New Revision: 39772

# import regulare expresion library
import re

# Open file to search in
fhand = open('mbox.txt')

# Execute regular expresion and print result
count = 0
total = 0

for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) > 0:
        count += 1        
        total += int(x[0])

average = total / count
print(int(average))

