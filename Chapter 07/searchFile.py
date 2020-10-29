fhand = open('mbox.txt')
count = 0
for line in fhand:
    line = line.rstrip()

    if line.find('@uct.ac.za') == -1: continue
    print(line)

    #if line.startswith('From:'):
        #print(line)
       #count = count + 1
#print('Number of email adresses:', count)