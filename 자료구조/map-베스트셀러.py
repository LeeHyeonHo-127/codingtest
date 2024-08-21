# boj 1302

books = dict()

for _ in range(int(input())):
    name = input()
    if name in books:
        books[name] += 1
    else:
        books[name] = 1

arr = []

max_val = max(books.values())

for k, v in books.items():
    if v == max_val:
        arr.append(k)

arr.sort()
print(arr[0])