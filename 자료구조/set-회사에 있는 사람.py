# boj 7785

import sys
input = sys.stdin.readline

s = set()

for _ in range(int(input())):
    n, el = input().split()
    if el == 'enter':
        s.add(n)
    else:
        if n in s:
            s.remove(n)

for name in sorted(s, reverse=True):
    print(name) 