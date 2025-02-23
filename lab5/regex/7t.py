import re
text = "hello_world_python"
result = re.sub(r'_(\w)', lambda m: m.group(1).upper(), text)
result = result[0].upper() + result[1:] 
print(result) 