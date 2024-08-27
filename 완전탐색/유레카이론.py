# boj10448

from itertools import combinations_with_replacement

arr = [1]
for i in range(2, 46):
    arr.append(arr[i-2]+i)

for _ in range(int(input())):
    result = 0
    num = int(input())
    for i in combinations_with_replacement(arr, 3):
        if (sum(i) == num):
            result = 1
    print(result)


# 3중 for문을 사용한 풀이 
# 중복조합을 사용해 푼 것 보다 훨씬 빠름 300ms vs 3000ms
arr = [n * (n+1)//2 for n in range(1,47)]

def is_possible(k):
    for i in range(0, 46):
        for j in range(0,46):
            for p in range(0,46):
                if arr[i] + arr[j] + arr[p] == k:
                    return 1
    return 0

for _ in range(int(input())):
    print(is_possible(int(input())))

