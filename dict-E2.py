# Exercise 2: Write a program that categorizes each mail message by which 
# day of the week the commit was done. To do this look for lines that start 
# with "From", then look for the third word and keep a running count of 
# each of the days of the week. At the end of the program print out the 
# contents of your dictionary (order does not matter).

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
days_dict = {}
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From' : continue
    try:
        days_dict[words[2]] = days_dict.get(words[2],0) + 1
    except:
        print("Something went wrong")

print(days_dict)