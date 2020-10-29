# Exercise 5: 
# This program records the domain name (instead of the address) where the 
# message was sent from instead of who the mail came from (i.e., the whole 
# email address). At the end of the program, print out the contents of your 
# dictionary.

# fname = input('Enter the file name: ')
fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

domains = {}

for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    try:
        domainStart = words[1].find('@') + 1
        domain = words[1][domainStart:]
        domains[domain] = domains.get(domain,0) + 1
    except:
        print("Something went wrong")

print(domains)