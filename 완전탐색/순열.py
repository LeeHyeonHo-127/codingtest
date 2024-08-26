from itertools import permutations

arr = [0, 1, 2, 3]

for i in permutations(arr, 4):
    print(i)

# n개중 r개를 뽑는 경우의 수(순서를 고려해서)
a = permutations(arr, 4)
print(len(list(a)))

