# function to calculate gross pay by hours and rate
def computepay(h, r):
    print("hours:", h, "rate:", r)
    if h <= 40:
        grossPay = r * h
    else:
        grossPay = 40 * r + (h - 40) * 1.5 * r
    return grossPay

# prompt for user to input their hours and rate
hrs = input("Enter Hours:")
rate = input("Pay rate:")

# returns error if they enter the wront data type
try:
    hf = float(hrs)
    rf = float(rate)
except:
    print('Error, please use numeric input')
    quit()

# calls the computepay function
p = computepay(hf, rf)

# prints amount of pay to the user
print("Pay", p)