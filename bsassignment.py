import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_454745.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tag
tags = soup('span')
sum = 0

for tag in tags:
    # Look at the parts of a tag
    #print(tag)
    #print(tag.contents)
    number = tag.contents[0]
    number = int(number)
    sum = sum + number

print(sum)

#print(numlist)
#print(sum)

#piece = re.findall('<span> class="comments">([0-9]+))', line)
