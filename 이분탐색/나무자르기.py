from bisect import bisect_left


def total_len(h):
    hap = 0
    l = bisect_left(tree, h)

    for i in range(l, len(tree)):
        p = tree[i] - h
        if p > 0:
            hap += p
    return hap

N, M = map(int, input().split())
tree = [int(num) for num in input().split()]
tree.sort()
left = 0
right = tree[len(tree) - 1]
mid = (right + left) // 2

while(True):
    t = total_len(mid)
    if t == M or right-left == 1: 
        break
    elif t > M:
        left = mid 
    elif t < M:
        right = mid
    mid = (left+right)//2

print(mid)

