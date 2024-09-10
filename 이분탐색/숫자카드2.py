# from bisect import bisect_left, bisect_right

# N = int(input())
# arr_n = list(map(int, input().split()))
# M = int(input())
# arr_m = list(map(int, input().split()))

# arr_n.sort()

# for i in arr_m:
#     print(bisect_right(arr_n, i) - bisect_left(arr_n, i), end=" ")


####
# map(dictionary)을 이용한 풀이
N = int(input())
cards = {}

for i in map(int, input().split()):
    if i in cards:
        cards[i] += 1
    else:
        cards[i] = 1
M = int(input())
ans = []
for i in map(int, input().split()):
    if i in cards:
        ans.append(cards[i])
    else:
        ans.append(0)
print(' '.join(map(str, ans)))




