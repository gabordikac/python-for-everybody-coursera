score = input("Enter Score: ")
try:
    s=float(score)
except:
    print('Value needs to be between 0.0 and 1.0')
    quit()

if score>=0.90:
    grade='A'
elif score>=0.80:
    grade='B'
elif score>=0.70:
    grade='C'
elif score>=0.60:
    grade='D'
else:
    grade='F'
print(grade)
