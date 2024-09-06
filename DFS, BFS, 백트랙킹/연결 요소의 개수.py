# boj 11724

import sys
sys.setrecursionlimit(10 ** 6) # 재귀 호출 제한 설정값은 1000이다. 이를 재설정 하기 위한 코드
input = sys.stdin.readline # 빠른 input을 위한 코드

N, M = map(int, input().split())
adj = [[False] * (N+1) for _ in range(N+1)]
chk = [False] * (N+1)
count = 0

def dfs(i):
    for j in range(1, N+1):
        if (adj[j][i] and not chk[j]):
            chk[j] = True
            # print(i, "일 때 ", j)
            dfs(j)

for _ in range(M):
    y, x = map(int, input().split())
    adj[y][x] = True
    adj[x][y] = True

# for k in range(0, N+1):
#     print(adj[k])


for i in range(1, N+1):
    if (not chk[i]):
        chk[i] = True
        count += 1
        dfs(i)

print(count)
