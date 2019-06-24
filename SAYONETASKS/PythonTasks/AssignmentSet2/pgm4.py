#Fetch data from the URL https://www.w3schools.com/xml/simple.xml and print name, price
#of each item


# ##Opening link and reading from API
import urllib.request
##reading XML
import xml.etree.ElementTree as ET
link="https://www.w3schools.com/xml/simple.xml"
f=urllib.request.urlopen(link)
data=f.read()
#print(data)
root=ET.fromstring(data)

for food in root.findall('food'):
    name=food.find('name').text
    price=food.find('price').text
    print(name,price)











#
# import xml.etree.ElementTree as ET
#
# import requests
#
# from xml.etree import ElementTree
# response = requests.get('https://www.w3schools.com/xml/simple.xml')
# tree = html.fromstring(response.content)
# #This will create a list of food name
# names = tree.xpath('//food/name/text()')
# #This will create a list of prices
# prices = tree.xpath('//food/price/text()')
# food = dict(zip(names,prices))
# print("Food items name and their prices : ",food)
#
