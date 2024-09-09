a = [2, 3, 6, 6, 8, 12]
left = 0
right = len(a) - 1
mid = (left + right) // 2
while left <= right:
    if a[mid] == 3:
        print(f'a[{mid}] = 3')
        break
    elif a[mid] > 3:
        right = mid - 1
    elif a[mid] < 3:
        left = mid + 1
    mid = (left + right) // 2