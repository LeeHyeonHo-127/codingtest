# boj 2178

from collections import deque


dy = (0, 1, 0, -1)
dx = (-1, 0, 1, 0)
dq = deque()

N, M = map(int, input().split())
miro = [ input() for _ in range(N) ]
chk = [[False] * M for _ in range(N)]
dq.append((0, 0, 1))
chk[0][0] = True

def is_valid(y, x):
    return 0 <= x < M and 0 <= y < N

while len(dq):
    y, x, d = dq.popleft()

    if y == N-1 and x == M-1:
        print(d)
        break

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if (is_valid(ny, nx) and miro[ny][nx] == '1' and not chk[ny][nx]):
            dq.append((ny,nx,d+1))
            chk[ny][nx] = True

