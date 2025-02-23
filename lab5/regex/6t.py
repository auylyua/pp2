import re
text = "blue banana apple base balance mouse orange"
print(re.sub(r'[ ,.]',':', text))  