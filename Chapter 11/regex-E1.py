# Exercise 1: 
# Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that 
# matched the regular expression:

# import regulare expresion library
import re

# Ask user for input
regex = input('Enter a regular expression: ')

# Open file to search in
fhand = open('mbox.txt')

# Execute regular expresion
count = 0

for line in fhand:
    line = line.rstrip()
    if re.search(regex, line):
        count += 1

# Print result
print('mbox.txt had', count, 'line that matched', regex)