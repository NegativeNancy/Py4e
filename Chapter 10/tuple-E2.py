# Exercise 2: 
# This program counts the distribution of the hour of the day for each of the 
# messages. You can pull the hour from the “From” line by finding the time 
# string and then splitting that string into parts using the colon character. 
# Once you have accumulated the counts for each hour, print out the counts, 
# one per line.

fname = input('Enter the file name: ')
try:
    if fname == str(''):
        fhand = open('mbox-short.txt')
    else:   
        fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

timeofday = dict()

# Retrieve hours from file and count them
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    try:
        if words[5][:2] not in timeofday: timeofday[words[5][:2]] = 1
        else: timeofday[words[5][:2]] += 1
    except:
        print("Something went wrong")

# Sort based on key
lst = list()
for key, value in list(timeofday.items()): lst.append((key, value))
lst.sort()

# Print hours sorted by frequency
for key, value in lst:
    print(key, value)
