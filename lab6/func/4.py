import math
import time
n = int(input("enter a number: "))
m = int(input("enter number in milliseconds: "))
print("Hmmmmm...🤔")
time.sleep(m/1000)
nsqrt = math.sqrt(n)
print(f'Square root of {n} after {m} miliseconds is {nsqrt}')