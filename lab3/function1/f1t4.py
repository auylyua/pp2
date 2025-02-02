def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtr(n):
    return [i for i in n if isprime(i)]

n = list(map(int, input("Enter numbers separated by space: ").split()))
print(filtr(n))