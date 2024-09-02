# boj 1931
import sys

input = sys.stdin.readline
arr = []
for _ in range(int(input())):
    start, end = map(int, input().split())
    # a, b = input().split()
    arr.append((start, end))

arr.sort(key=lambda x:(x[1], x[0]), reverse=True)
# print(arr)

p = arr.pop()
last_end = p[1]
end = p[1]
cnt = 1
while(len(arr)>0):
    p = arr.pop()
    if(last_end <= p[0]):
        last_end = p[1]
        cnt += 1
        # print("cnt ++ 일 때의 회의시간", p)

print(cnt)

        
