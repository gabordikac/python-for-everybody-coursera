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
    if (h.isdigit() and r.isdigit()):
        break
    else:
        print("I need numeric value")

p = computepay(h,r)
print("Pay",p)
