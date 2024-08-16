# n = int(input())

# for i in range(n):
#     temp = []
#     input_char = list(input())
#     temp.append(input_char.pop())

#     while(len(input_char) != 0):
#         a = input_char.pop()
#         if (len(temp) == 0):
#             temp.append(a)
#         else:
#             b = temp.pop()
#             if(a == b):
#                 temp.append(b)
#                 temp.append(a)

#     if(len(temp) == 0):
#         print("YES")
#     else:
#         print("NO")


for _ in range(int(input())):
    ans = "YES"
    stk = []
    for c in input():
        if c == '(' :
            stk.append(c)
        else:
            if(len(stk) == 0):
                ans = "NO"
            else:
                stk.pop()
    print(stk)
    if (len(stk) > 0):
        ans = "NO"
    print(ans)