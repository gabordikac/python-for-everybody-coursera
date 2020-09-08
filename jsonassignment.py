import urllib.request, urllib.parse, urllib.error
import json

data = input('Enter location: ')
js = urllib.request.urlopen(data).read()
#print(js)

info = json.loads(js)
#print('INFO: ', info)

count = 0
total_count = 0

for item in info['comments']:
    #print('Numbers: ', item['count'])
    count += 1
    total_count = total_count + item['count']

print('Count: ', count)
print('Sum: ', total_count)
