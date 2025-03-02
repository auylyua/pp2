from functools import reduce
def multiply(numders):
    return reduce(lambda x,y: x*y , numders)
print(multiply([1,3,5,7,9]))