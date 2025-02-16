def div(a,b,n):
    for i in range(n+1):
        if i % a == 0 and i % b == 0:      
            yield i

n = int(input())
a = int(input())
b = int(input())
for i in div(a,b,n):
    print(i, end=" ")
