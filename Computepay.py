print("hello")
def computepay(h,r):
    if h>40:
        rhrs = 40*r
        ohrs = (h-40) * (r*1.5)
        pay = rhrs+ohrs
    else:
        pay = h*r
    return pay

print("csao")
hrs = input("Enter Hours:")
rate = input("Enter Hourly Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print('Please enter a numeric value')

print("Pay",computepay(h,r))
