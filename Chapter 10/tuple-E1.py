# Exercise 1:
# Revise a previous program as follows: Read and parse the “From” lines and pull 
# out the addresses from the line. Count the number of messages from each person
# using a dictionary.

# After all the data has been read, print the person with the most commits by 
# creating a list of (count, email) tuples from the dictionary. Then sort the 
# list in reverse order and print out the person who has the most commits.

fname = input('Enter the file name: ')
try:
    if fname == str(''):
        fhand = open('mbox-short.txt')
    else:   
        fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

emailadresses = dict()

# Retrieve email addresses from file
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    try:
        if words[1] not in emailadresses: emailadresses[words[1]] = 1
        else: emailadresses[words[1]] += 1
    except:
        print("Something went wrong")

# Sort based on value
lst = list()
for key, value in list(emailadresses.items()): lst.append((value, key))
lst.sort(reverse=True)

# Print user with max value
maxMails, maxUser = lst[0]
print(maxUser, maxMails)
