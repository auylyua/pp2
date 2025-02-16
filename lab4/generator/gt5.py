def cou(b):
    for i in range(b,-1,-1):   
        yield i
b = int(input())
for i in cou(b):
    print(i, end=" ")