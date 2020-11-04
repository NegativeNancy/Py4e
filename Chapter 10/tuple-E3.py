# Exercise 3: 
# Write a program that reads a file and prints the letters in decreasing order 
# of frequency. Your program should convert all the input to lower case and only 
# count the letters a-z. Your program should not count spaces, digits, 
# punctuation, or anything other than the letters a-z. Find text samples 
# from several different languages and see how letter frequency varies between 
# languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string

fname = input('Enter the file name: ')
try:
    if fname == str(''):
        fhand = open('text-programmeren.txt')
    else:   
        fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

letters = dict()

# Retrieve hours from file and count them
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    if len(words) == 0: continue
    for word in words:
        for char in word:
            if char.isalpha() == True:
                if char not in letters: letters[char] = 1
                else: letters[char] += 1

# # Sort based on key
lst = list()
for key, value in list(letters.items()): lst.append((key, value))
lst.sort()

# Print hours sorted by frequency
for key, value in lst:
    print(key, value)
