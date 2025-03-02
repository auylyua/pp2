def is_palyndrom(text):
    return text == text[::-1]

text = input("enter a text: ")
if is_palyndrom(text):
    print("TRUE")
else:
    print("FALSE")