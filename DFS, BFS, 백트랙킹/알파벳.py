# 내 풀이

from collections import deque
import copy

# def is_valid(y, x, al):
#     return 0 <= x < C and 0 <= y < R and not board[y][x] in al

# dx = (-1, 0, 1, 0)
# dy = (0, 1, 0, -1)
# R, C = map(int, input().split())
# board = [input() for _ in range(R)]
# dq = deque()
# dq.append(([0, 0], [board[0][0]], 1))

# while(True):
#     pos, al, n = dq.popleft()
#     for i in range(4):
#         nx = pos[1] + dx[i]
#         ny = pos[0] + dy[i]
#         nn = n + 1
#         if(is_valid(ny, nx, al)):
#             nal = copy.deepcopy(al)
#             nal.append(board[ny][nx])
#             # print(ny, " ", nx, " ", nal, " ", nn)
#             dq.append(([ny, nx], nal, nn))
#     if len(dq) == 0:
#         print(n)
#         break
        
##### 책 코드

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

R, C = map(int, input().split())
board = [input() for _ in range(R)]
chk = [[set() for _ in range(C)] for _ in range(R)]
ans = 0

def is_valid_coord(y, x):
    return 0 <= x < C and 0 <= y < R

dq = deque()

chk[0][0].add(board[0][0])
dq.append((0, 0, board[0][0]))
while dq:
    y, x, s = dq.popleft()
    ans = max(ans, len(s))

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and board[ny][nx] not in s:
            ns = s + board[ny][nx]
            print("ns = ", ns)
            if ns not in chk[ny][nx]:
                chk[ny][nx].add(ns) # 가지치기의 핵심!! 내가 이 부분 고려를 못했다. 
                                    # 만약 ABE
                                    #     BCF 
                                    # 의 board가 있을 때, A를 기준으로 우측, 하단을 통해 C에 접근할 때의 경로는 둘 다 ABC가 된다. 
                                    # 만약 둘 다 큐에 넣는다면 연산이 2배로 걸릴 것이다. 내 상단의 코드가 그러했다. 
                                    # 이 코드는 특정 지점으로 도착하는 경로를 2차원 배역에 저장하고 이를 확인하여 같을 경우 큐에 넣지 않는다. 즉, 가지치기를 진행한다.
                                    # 이 부분을 고려하는게 백트래킹의 요소를 활용한 문제의 핵심이었다.
                dq.append((ny, nx, ns))

print(ans)




