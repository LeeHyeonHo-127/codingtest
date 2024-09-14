# boj 11726

import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())
cache = [0] * (n+1)

def dp(x):
    if cache[x] != 0:
        return cache[x]
    
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        cache[x] = (dp(x-1) + dp(x-2)) % 10007
        return cache[x]
    
print(dp(n))