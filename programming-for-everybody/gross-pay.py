hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print('Error, please use numeric input')
    quit()

print("hours:", h, "rate:", r)
if h <= 40:
    grossPay = r * h
else:
    grossPay = 40 * r + (h - 40) * 1.5 * r
print("pay:", grossPay)