import re
text = "hello_world python_is_fun snake_case 2nd defendens"
print(re.findall(r'[a-z]+_[a-z]+', text))
