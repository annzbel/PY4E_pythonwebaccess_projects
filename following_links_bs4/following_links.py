#Assigmnent to read HTML files, extract anchor tags, finds name in a given position, follows the link and find the name in the new link in a given position. Then to generate the list of names.
#sample URL http://py4e-data.dr-chuck.net/known_by_Fikret.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re 

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the URL: ')
position = int(input('Enter position: '))
count = int(input('Enter how many times: '))

print('Retrieving:', url) 
names_list = []


for i in range(0, count): #looping through 'count' number of times
    html = urllib.request.urlopen(url, context=ctx).read() #reading through the URL 
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a') #will give a list of anchor tags
    tag = tags[position - 1] #finding in position given by end user
    next_url = tag.get('href', None) #retrieving url
    name = re.findall('known_by_(.*)?\.', next_url) #fine-tuned to just get name

    names_list.append(name)
    print( 'Retrieving:', next_url)
    url = next_url  #replacing url to run next 
    

    
