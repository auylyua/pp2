def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print("The word/phrase is a palindrome.")
else:
    print("The word/phrase is not a palindrome.")
