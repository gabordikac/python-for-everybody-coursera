import re
text = open('regexassignment.txt')
#print(text.read())

all_numbers = re.findall('[0-9]+', text.read())
all_numbers = list(map(int, all_numbers))

#print('Numbers: ', all_numbers)
print(sum(all_numbers))
