# boj 11724

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[False]*(N+1) for _ in range(N+1)]
chk = [False] * (N+1)
count = 0

def dfs(k):
    for i in range(1, N+1):
        if adj[i][k] and not chk[i]:
            chk[i] = True
            dfs(i)


for _ in range(M):
    y, x = map(int, input().split())
    adj[x][y] = True
    adj[y][x] = True

for i in range(1, N+1):
    if not chk[i]:
        chk[i] = True
        count += 1
        dfs(i)

print(count)
