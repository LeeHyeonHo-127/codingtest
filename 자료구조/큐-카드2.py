# boj 2164

from collections import deque

card = deque(range(1,int(input())+1))
while(len(card) > 1):
    card.popleft()
    temp = card.popleft()
    card.append(temp)
print(card[0])
    
