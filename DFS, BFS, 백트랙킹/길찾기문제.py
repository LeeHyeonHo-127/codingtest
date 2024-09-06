from collections import deque

dy = (0, 1, 0, -1)
dx = (-1, 0, 1, 0)
N = int(input())
chk = [[False] * N for _ in range(N)]

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

def dfs(y, x):
    if adj[y][x] == ans:
        return
    
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and not chk[ny][nx]:
            chk[ny][nx] = True
            dfs(ny, nx)


def bfs(sy, sx): # start y, x
    q = deque()
    chk[sy][sx] = True
    q.append((sy, sx))
    while len(q):
        y, x = q.popleft()
        if adj[y][x] == ans:
            return
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append(ny, nx)