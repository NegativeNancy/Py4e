fname = input('Enter the file name: ')

if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    exit()

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

keyword = 'X-DSPAM-Confidence:'
length = len(keyword)
count = 0
sum = 0

for line in fhand:
    if line.startswith(keyword):
        line = line.rstrip()

        count = count + 1
        sum = sum + float(line[length:])

average = sum / count

print('Average spam confidence: ', average)

