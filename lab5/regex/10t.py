import re
with open(r'C:\pp2\lab5\regex\t.txt') as file:
    text = file.read() 
r=re.sub(r'([a-z])([A-Z])',r'\1_\2',text).lower()
print(r) 