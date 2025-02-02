def revrs(s):
    w = s.split() 
    w.reverse()
    return " ".join(w)  

s = input("Enter a sentence: ")
print(revrs(s))
