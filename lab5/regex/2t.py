import re
text = "apple a abb abbb abc abbbb "
print(re.findall(r'ab{2,3}', text))  