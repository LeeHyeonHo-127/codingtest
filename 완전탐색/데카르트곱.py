from itertools import product

a = ['123', 'abc', "!@#"]
pd = list(product(*a))
print(pd)