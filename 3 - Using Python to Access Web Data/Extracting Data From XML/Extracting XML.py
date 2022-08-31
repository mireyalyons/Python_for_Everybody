#first version
#import urllib.request, urllib.parse, urllib.error
#import xml.etree.ElementTree as ET
#url = ‘http://py4e-data.dr-chuck.net/comments_269101.xml’
#uh = urllib.request.urlopen(url)
#data = uh.read()
#tree = ET.fromstring(data)
#counts = tree.findall(‘.//count’)
#counts_list = [int(count.text) for count in counts]
#print(sum(counts_list))




#version i like better
#import urllib.request, urllib.parse, urllib.error
#import xml.etree.ElementTree as ET

#url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

#uh = urllib.request.urlopen(url)
#data = uh.read()

#tree = ET.fromstring(data)

#lst = tree.findall('comments/comment/count')

#counts = tree.findall('.//count')

#for each in counts:
#    print(each.text)

from urllib import request
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1419498.xml'
print ("Retrieving", url)
html = request.urlopen(url)
data = html.read()
print("Retrieved",len(data),"characters")

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
count=len(results)
sum=0

for result in results:
    sum += float(result.find('count').text)
print(count)
print(sum)
