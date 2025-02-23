import re
text = "USA Hello ABCworld XMLParser"
print(re.findall(r'[A-Z][a-z]+', text))
