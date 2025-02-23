import re
with open(r'C:\pp2\lab5\regex\t.txt') as file:
    text = file.read() 
print(re.findall(r'ab{2,3}', text))  