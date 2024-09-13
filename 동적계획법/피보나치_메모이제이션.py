cache = [-1] * 37

def f(n):
    if cache[n] != -1:
        return cache[n]
    
    cache[n] = n if n < 2 else f(n-1)+f(n-2)
    return cache[n]

print(f(10))