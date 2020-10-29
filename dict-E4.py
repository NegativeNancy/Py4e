# Exercise 4: 
# Add code to the above program to figure out who has the most messages in 
# the file. After all the data has been read and the dictionary has been 
# created, look through the dictionary using a maximum loop (see Chapter 5: 
# Maximum and minimum loops) to find who has the most messages and print how 
# many messages the person has.

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

maxMails = 0
maxUser = None

for key in emailadresses:
    if emailadresses.get(key) > maxMails:
        maxMails = emailadresses[key]
        maxUser = key


print(maxUser, maxMails)