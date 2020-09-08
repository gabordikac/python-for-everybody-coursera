import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter location: ')
xml = urllib.request.urlopen(url).read()

#print(xml)

commentinfo = ET.fromstring(xml)

#retreiving <count> values from <comment> tags
lst = commentinfo.findall('comments/comment')
print("Count: ", len(lst))


numbers_total = 0

for comment in lst:
    count = comment.find('count').text
    #print('Text in count: ', count)
    numbers_total = numbers_total + int(count)

print('Sum: ', numbers_total)
