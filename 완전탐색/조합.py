from itertools import combinations

arr = [1,2,3,4]

for i in combinations(arr, 3):
    print(i)

# n개중 r개를 순서를 고려하지 않고 고르는 경우의 수
print(len(list(combinations(arr, 3))))