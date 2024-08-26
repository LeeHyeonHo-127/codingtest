# boj 3040

from itertools import combinations

# arr = []
# for i in range(9):
#     arr.append(int(input()))

# for i in combinations(arr,7):
#     if (sum(i) == 100):
#         for r in i:
#             print(r)
#         break

for i in combinations([int(input()) for _ in range(9)], 7):
    if (sum(i)==100):
        for j in sorted(i):
            print(j)
        break