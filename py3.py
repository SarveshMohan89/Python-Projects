import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
sum = 0

url = 'http://py4e-data.dr-chuck.net/comments_419684.xml'
head = urllib.request.urlopen(url)
data = head.read()

tree = ET.fromstring(data)

lst = tree.findall('comments/comment/count')

counts = tree.findall('.//count')

total = 0

for count in counts:
    total += int(count.text)

print('total: ', total)
