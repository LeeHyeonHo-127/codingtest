coords = [False] * 1001
ans = 0
i = 0
N, L = map(int, input().split()) # 두 값을 받아서 정수형으로 각 변수에 대입할 때
for k in map(int, input().split()):
    coords[k] = True

# print(coords)

while(i<1001):
    # print("현재 = ", i)
    
    if (coords[i]):
        ans += 1
        # print("현재 ", i, "일 때 ans += 1 그리고 i += L = ", i+L)
        i += L
        print(i)
    else:
        i += 1
print(ans)