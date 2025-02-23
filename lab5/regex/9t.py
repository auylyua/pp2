import re
with open(r'C:\pp2\lab5\regex\t.txt') as file:
    text = file.read() 
print(re.sub(r'([a-z])([A-Z])',r'\1 \2', text))  