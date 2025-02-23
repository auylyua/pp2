import re
text = "HelloWorld Python JavaScript"
print(re.sub(r'([a-z])([A-Z])',r'\1 \2', text))  