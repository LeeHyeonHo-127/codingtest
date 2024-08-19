import heapq

h = []
heapq.heappush(h, 123)
heapq.heappush(h, 423)
heapq.heappush(h, 323)

while len(h):
    print(heapq.heappop(h))