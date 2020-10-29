def computepay(h,r):
    if h > 40 :
        extraHours = h - 40
        extraRate = r * 1.5
    
        normalPay = 40 * r
        extraPay = extraHours * extraRate

        pay = normalPay + extraPay
    else:
    	pay = h * r
        
    return pay

try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    p = computepay(hrs, rate)
    print("Pay:", p)
except:
    print('Error, please enter numeric input') 
