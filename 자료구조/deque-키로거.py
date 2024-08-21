# boj 5387

from collections import deque
import sys

input = sys.stdin.readline


for _ in range(int(input())):
    pw = input()
    ldq = deque()
    rdq = deque()
    result = []
    for i in pw:
        if(i.isalnum()):
            # print(i, " 를 ldq에 append")
            ldq.append(i)           
        elif (i == '<' and len(ldq) != 0):
            rdq.append(ldq.pop())
        elif (i == '>' and len(rdq) != 0):
            ldq.append(rdq.pop())
        elif (i == '-' and len(ldq) != 0):
            ldq.pop()
    print(''.join(ldq) + ''.join(reversed(rdq)))
