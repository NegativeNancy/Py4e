str = 'X-DSPAM-Confidence:0.8475'

sliced = str.find(':') + 1
number = float(str[sliced:])

print(number)

number2 = str.split(':')
print(number2)

number3 = float(number2[1])
print(number3)
