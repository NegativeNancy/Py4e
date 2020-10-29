# Exercise 3: 
# Write a program to read through a mail log, build a histogram using a 
# dictionary to count how many messages have come from each email address, 
# and print the dictionary.

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

emailadresses = {}

for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    try:
        emailadresses[words[1]] = emailadresses.get(words[1],0) + 1
    except:
        print("Something went wrong")

print(emailadresses)