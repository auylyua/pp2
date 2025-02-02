def histogram(numbers):
    for num in numbers:
        print('*' * num)
n = list(map(int, input().split()))
histogram(n)
