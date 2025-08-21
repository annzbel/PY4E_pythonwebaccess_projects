#Web parsing with BeautifulSoup to calculate the sum of all numbers in the URL
#URL  http://py4e-data.dr-chuck.net/comments_1867730.html for assignment to test (answer 1997)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the URL: ')
html = urllib.request.urlopen(url, context=ctx).read() #reading through the URL 
soup = BeautifulSoup(html, 'html.parser')

import re  #importing the regex library 

#retrieve all table row with all lines by parsing all starting with tr, using soup 
tr = soup('tr')
tr = str(tr) #making it a string so i can use re to find numbers 


sum = 0 #starting count
for lines in tr:
    numbers = re.findall('[0-9]+', tr) #using re to findall numbers in tr

for num in numbers: #looping through the numbers list
    num = int(num) #making each list variable an integer so can sum them together 
    sum = sum + num #adding each num in numbers to the sum/count

print(sum) #printing the final count 

