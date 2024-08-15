# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from collections import deque
import heapq
import sys
from itertools import permutations
from itertools import combinations

# 순열 라이브러리 사용해보기
def permutation():
    arr = [1,2,3,4]
    print(len(list(permutations(arr, 2))))

# 조합 라이브러리 사용해보기
def combination():
    arr = [1,2,3,4]
    print(len(list(combinations(arr,2))))


# 백설 공주와 일곱 난쟁이
def boj3040():
    for i in combinations( [ int(input()) for _ in range(9) ], 7):
        if sum(i) == 100:
            for j in i:
                print(j)
            break


# 유레카 이론
def boj10448():
    T = [n * (n + 1) // 2 for n in range(46)]



    def is_possible(num):
        for i in range(1, 46):
            for j in range(1, 46):
                for k in range(1, 46):
                    if T[i] + T[j] + T[k] == num:
                        return 1

        return 0

    for i in range(int(input())):
        print(is_possible(int(input())))


# 사탕 게임
def boj3085():

    N = int(input())
    board = [list(input()) for _ in range(N)]
    ans = 1

    def search():
        nonlocal ans
        for i in range(N):
            cnt = 1
            for j in range(1, N):
                if board[i][j-1] == board[i][j]:
                    cnt += 1
                    ans = max(ans, cnt)
                else:
                    cnt = 1

        for j in range(N):
            cnt = 1
            for i in range(1,N):
                if board[i-1][j] == board[i][j]:
                    cnt += 1
                    ans = max(ans, cnt)
                else:
                    cnt = 1

    for i in range(N):
        for j in range(N):
            if j + 1 < N :
                board[i][j], board[j][j+1] = board[i][j + 1], board[i][j]
                search()
                board[i][j], board[j][j + 1] = board[i][j + 1], board[i][j]

            if i + 1 < N :
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                search()
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

    print(ans)









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    boj3085()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
