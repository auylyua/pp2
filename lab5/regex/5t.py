import re
text = "apple a abb abbb abc abbbb "
print(re.findall(r'a.*b', text))  