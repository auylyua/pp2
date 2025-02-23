import re
with open(r'C:\pp2\lab5\regex\t.txt') as file:
    text = file.read() 
print(re.findall(r'\b[a-z]+_[a-z]+', text))
