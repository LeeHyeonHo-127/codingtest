fibo = [-1]*37
for i in range(37):
    fibo[i] = i if i < 2 else fibo[i-1] + fibo[i-2]

print(fibo[36])