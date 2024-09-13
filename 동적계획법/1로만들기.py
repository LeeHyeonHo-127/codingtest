import sys
sys.setrecursionlimit(10 ** 6)
INF = 987654321
N = int(input())
cache = [INF] * (N + 1)
cache[1] = 0

def dp(x):
    if cache[x] != INF :
        return cache[x]
    
    if x % 6 == 0:
        cache[x] = min(dp(x // 3)+1, dp(x // 2)+1)
    elif x % 3 == 0:
        cache[x] = min(dp(x // 3)+1 , dp(x - 1)+1)
    elif x % 2 == 0:
        cache[x] = min(dp(x //2)+1, dp(x-1)+1)
    else:
        cache[x] = dp(x-1)+1
    return cache[x]

print(dp(N))
    
# BFS를 활용한 풀이
from collections import deque

N = int(input())
dq = deque()
dq.append((N, 0))
chk = [False] * (N+1)
chk[N] = True

while dq:
    x, d = dq.popleft()
    if x == 1:
        print(d)
        break

    if x % 3 ==0 and not chk[x//3]:
        dq.append((x//3, d+1))
        print(x//3, " ", d+1)
        chk[x // 3] = True
    
    if x % 2 == 0 and not chk[x//2]:
        dq.append((x//2, d+1))
        print(x//2, " ", d+1)
        chk[x//2] = True
    
    if not chk[x-1]:
        dq.append((x-1, d+1))
        print(x-1, " ", d+1)
        chk[x-1] = True