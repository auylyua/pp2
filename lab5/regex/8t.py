import re
text = "hello_world python_is_fun snake_case 2nd defendens"
print(re.findall(r'[A-Z][a-z]*', text))
