import re
with open(r'C:\pp2\lab5\regex\t.txt') as file:
    text = file.read() 
result = re.sub(r'_(\w)', lambda m: m.group(1).upper(), text)
result = result[0].upper() + result[1:] 
print(result) 