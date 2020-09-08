largest = -1
print('Before', largest)
for value in [9, 41, 12, 3, 74, 15]:
    if value > largest:
        largest = value
    print(value, largest)
print('After', largest)
