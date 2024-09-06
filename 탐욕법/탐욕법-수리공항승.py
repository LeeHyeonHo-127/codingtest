# boj 1449

# N, L = map(int, input().split()) # 두 값을 받아서 정수형으로 각 변수에 대입할 때
# arr = list(map(int, input().split())) # 여러 값을 받아서 정수형 배열에 넣을 때
# arr.sort()

# T = (0, 0)
# count = 0
# for h in arr:
#     if not ((h-0.5) >= T[0] and h+0.5 <= T[1]):
#         print("고장지점 = ",h)
#         T = (h-0.5, h-0.5+L)
#         count += 1
# print(count)


    
# ---

coords = [False] * 1001
ans = 0
i = 0
N, L = map(int, input().split()) # 두 값을 받아서 정수형으로 각 변수에 대입할 때
for k in map(int, input().split()):
    coords[k] = True

while(i<1001):    
    if (coords[i]):
        ans += 1
        i += L
    else:
        i += 1
print(ans)



