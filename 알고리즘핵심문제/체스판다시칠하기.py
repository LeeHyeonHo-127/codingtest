# boj 1018
# 완전 탐색 1
M, N = map(int, input().split())
board = [input() for _ in range(M)]
bc = 987654321
pc = 987654321

for i in range(M-7):
    for j in range(N-7):
        for s in range(2):
            bc = min(bc, pc)
            pc = 0
            if s == 0:
                temp = 'W'
                if temp != board[i][j]: pc += 1
            else:
                temp = 'B'
                if temp != board[i][j]: pc += 1                

            for k in range(i, i+8):
                if k != i:
                    temp = 'W' if temp == 'B' else 'B'
                for m in range(j, j+8):
                    if k != i or m != j:
                        # print("현재 : [%d][%d] = %d", k, m, board[k][m], "temp = %d", temp)
                        if temp == board[k][m]:
                            # print("같다!")
                            # print("pc = ", pc)
                            pc += 1
                            temp = 'W' if temp == 'B' else 'B'
                        else:
                            temp = board[k][m]

print(min(bc, pc))


# 완전 탐색 2
M, N = map(int, input().split())
board = [input() for _ in range(N)]
ans = N*M

def fill(y, x, bw):
    global ans
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i*j) % 2:
                if board[y + i][x + i] == bw:
                    cnt += 1
            else:
                if board[y + i][x + i] != bw:
                    cnt += 1
    ans = min(ans, cnt)

for y in range(N-7):
    for x in range(M-7):
        fill(y, x, 'B')
        fill(y, x ,'W')

print(ans)


# 누적합

N, M = map(int, input().split())
board = [input() for _ in range(N)]
ans = N * M

def make_acc(bw):
    global ans
    acc = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i > 0:
                acc[i][j] +=  acc[i-1][j]
            if j > 0:
                acc[i][j] += acc[i][j-1]
            if i > 0 and j > 0:
                acc[i][j] -= acc[i-1][j-1]
            if (i + j) % 2 and board[i][j] == bw:
                acc[i][j] += 1
            if (i + j) % 2 == 0 and board[i][j] != bw:
                acc[i][j] += 1
    
    for i in range(N-7):
        for j in range(M-7):
            cnt = acc[i+7][j+7]
            if i > 0:
                cnt -= acc[i-1][j+7]
            if j > 0:
                cnt -= acc[i+7][j-1]
            if i > 0 and j > 0:
                cnt += acc[i-1][j-1]
            ans = min(ans, cnt)

make_acc('B')
make_acc('W')
print(ans)