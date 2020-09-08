hrs=input('Enter Hours:')
hwage=input('Enter Hourly Rate:')
try:
    h=float(hrs)
    hw=float(hwage)
except:
    print("Need to be a number")
    quit()

if h>40:
    reghrs=h*hw
    overhrs=(h-40)*(hw*0.5)
    fullpay=reghrs+overhrs
else:
    fullpay=h*hw
print(fullpay)
