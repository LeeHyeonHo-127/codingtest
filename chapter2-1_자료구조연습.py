# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from collections import deque
import heapq
import sys

def print_hi(name):
    a1 = [[0] * 5] * 3
    a1[1][1] = 99
    print(a1)


    a2 = [[0] * 5 for _ in range(3)]
    a2[1][1] = 99
    print(a2)

# 요세푸스 문제
def boj11866():
    N, K = map(int, input().split())
    peo = [i for i in range(1, N+1)]
    pt = 0
    ans = []

    for _ in range(N):
        pt += K - 1
        pt %= len(peo)
        ans.append(peo.pop(pt))

    print(f"<{', '.join(map(str, ans))}>")

# 괄호 문제
def boj9012():
    for _ in range(int(input())):
        stk = []
        ans = 'YES'
        array = input()
        for c in array:
            if c == '(':
                stk.append(c)
            else:
                if len(stk) > 0:
                    stk.pop()
                else:
                    ans = 'NO'

        if len(stk) > 0:
            ans = 'NO'

        print(ans)

def testDeque():
    dq = deque()
    dq.append(123)
    dq.append(456)
    dq.append(789)

    while len(dq):
        print(dq.popleft())

# 카드 2
def boj1264():
    dq = deque()

    for i in range(1, int(input()) + 1):
        dq.append(i)

    while len(dq) > 1:
        dq.popleft()
        dq.append(dq.popleft())

    print(dq.popleft())


# 우선순위큐 연습
def heapqTest():
    h = []
    heapq.heappush(h, 123)
    heapq.heappush(h, 456)
    heapq.heappush(h, 333)
    while len(h):
        print(heapq.heappop(h))


# 절댓값 힙
def boj11286():
    input = sys.stdin.readline
    hq = []
    for _ in range(int(input())):
        x = int(input())
        if x == 0:
            print(heapq.heappop(hq)[1] if len(hq) else 0)
        else :
            heapq.heappush(hq, (abs(x), x))

def boj11286_2():
    input = sys.stdin.readline

    min_heap = []
    max_heap = []

    for _ in range(int(input())):
        x = int(input())

        if x > 0 :
            heapq.heappush(min_heap, x)
        elif x < 0 :
            heapq.heappush(max_heap, -x)
        else :
            if len(min_heap):
                if len(max_heap) == 0 or min_heap[0] < max_heap[0]:
                    print(heapq.heappop(min_heap))
                else :
                    print(-heapq.heappop(max_heap))
            else :
                print(-heapq.heappop(max_heap) if len(max_heap) else 0)

# 베스트셀러
def boj1302():
    books = dict()
    for _ in range(int(input())):
        name = input()
        if name in books :
            books[name] += 1
        else :
            books[name] = 1

    max_val = max(books.values())
    arr = []
    for k, v in books.items():
        if v == max_val:
            arr.append(k)

    arr.sort()
    print(arr[0])

# 회사에 있는 사람

def boj7785():

    input = sys.stdin.readline
    s = set()

    for _ in range(int(input())):
        name, el = input().split()
        if el == 'enter':
            s.add(name)
        else:
            if name in s:
                s.remove(name)

    for name in sorted(s, reverse = True):
        print(name)


def boj5397():
    n = int(input())

    for _ in range(n):
        left = []
        right = []
        cmd = input()

        for i in cmd:
            if i == '<':
                if left:
                    right.append(left.pop())
            elif i == '>':
                if right:
                    left.append(right.pop())
            elif i == '-':
                if left:
                    left.pop()
            else:
                left.append(i)
        left.extend(reversed(right))

        print(''.join(left))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    boj5397()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
