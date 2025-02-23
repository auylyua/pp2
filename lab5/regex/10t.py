import re
text = "ConvertMe ToSnakeCase"
r=re.sub(r'([a-z])([A-Z])',r'\1_\2',text).lower()
print(r) 