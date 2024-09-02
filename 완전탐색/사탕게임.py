def def_max_raw(k):
    temp = 1
    max = 1
    for i in range(1, n):
        if(arr[k][i] == arr[k][i-1]):
            temp = temp + 1
            if(temp > max): max = temp
        else:
            temp = 1
    return max

def def_max_col(k):
    temp = 1
    max = 1
    for i in range(1, n):
        if(arr[i][k] == arr[i-1][k]):
            temp = temp + 1
            if(temp > max): max = temp
        else:
            temp = 1
    return max

n = int(input())
arr = [list(input()) for _ in range(n)]
max_raw = []
max_col = []
total_max = 0

for i in range(n):
    temp = def_max_raw(i)
    total_max = max(total_max, temp)
for j in range(n):
    temp = def_max_col(j)
    total_max = max(total_max, temp)


for i in range(n):
    for j in range(n-1):
        if (i < n-1):
            if(arr[i][j] != arr [i][j+1]):
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
                total_max = max(max(def_max_col(j), def_max_col(j+1),def_max_raw(i)), total_max)
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            if(arr[i][j] != arr[i+1][j]):
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
                total_max = max(max(def_max_raw(i), def_max_raw(i+1), def_max_col(j)), total_max)
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
        else:
            if(arr[i][j] != arr [i][j+1]):
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
                total_max = max(max(def_max_col(j), def_max_col(j+1),def_max_raw(i)), total_max)
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

print(total_max)
