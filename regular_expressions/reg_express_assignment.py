import re
count = 0
fh = open("regex_sum_1867728.txt")
for line in fh:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    if len(y) <1 : continue
    else:
        for items in y:
            count = count + int(items)
            #print(items)
     
print(count)
 
    
    
