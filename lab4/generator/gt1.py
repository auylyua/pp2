def sq(n):
    for i in range(n + 1):
        yield i ** 2

n = int(input())
for square in sq(n):
    print(square, end=" ")
