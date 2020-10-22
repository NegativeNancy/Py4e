hrs = input("Enter Hours: ")
h = float(hrs)

r = float(input("Enter Rate: "))

if h > 40 :
    extraHours = h - 40
    extraRate = r * 1.5
    
    normalPay = 40 * r
    extraPay = extraHours * extraRate
    
    pay = normalPay + extraPay
    
else:
	pay = h * r

print(pay)