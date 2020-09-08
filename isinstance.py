def computepay(h,r):
    if h>40:
        rhrs = 40*r
        ohrs = (h-40) * (r*1.5)
        return rhrs+ohrs
    else:
        return h*r

while True:
    hrs = input("Enter Hours: ")
    rate = input("Enter Hourly Rate: ")
    if (isinstance(float(hrs), (int, float)) and isinstance(float(rate), (int, float))):
        break
    else:
        print("I need numeric value")

p = computepay(float(hrs),float(rate))
print("Pay",p)
