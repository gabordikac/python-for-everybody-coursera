largest = -1
print('Before', largest)
for value in [7, 2, 10, 4]:
    if value > largest:
        largest = value
    print(value, largest)
print('After', largest)
