def histogram(numbers):
    for num in numbers:
        print('*' * num)
n = list(map(int, input().split()))
histogram(n)

import math
def volume(r):
    v = (4/3) * math.pi * (r ** 3)
    return v

radius = float(input())
print(volume(radius))


def oun(g):
    print(28.3495231 * g)
g=int(input())
oun(g)