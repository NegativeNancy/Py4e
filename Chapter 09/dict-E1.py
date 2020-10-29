# Exercise 1: 
# Download a copy of the file www.py4e.com/code3/words.txt 
# Write a program that reads the words in words.txt and stores them as keys 
# in a dictionary. It doesn't matter what the values are. Then you can use 
# the in operator as a fast way to check whether a string is in the dictionary.

fname = input('Enter the file name: ')
word_dict = {}
count = 1

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) == 0: continue
    for word in words:
        # print(word)
        word_dict[word] = count
        # print(word_dict)
        count = count + 1

print('Is the word \'program\' in dict?', 'program' in word_dict)