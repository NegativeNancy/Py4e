fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

keyword = 'X-DSPAM-Confidence:'
length = len(keyword)
count = 0
total = 0

for line in fhand:
    if line.startswith(keyword):
        line = line.rstrip()

        count = count + 1
        total = total + float(line[length:])

average = total / count

print('Average spam confidence: ', average)


