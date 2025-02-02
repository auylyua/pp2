class prime:
    def __init__(self, n):
        self.n = n  
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    def filtr(self):
        return list(filter(lambda x: self.is_prime(x), self.n))
n = list(map(int, input().split()))
fltr = prime(n)
print(fltr.filtr())
