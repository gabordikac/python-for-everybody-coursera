import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('http://www.dr-chuck.com/page1/htm')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve alll of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
