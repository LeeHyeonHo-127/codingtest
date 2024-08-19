# boj 11286

import heapq, sys

########### 튜플을 우선순위 큐에 넣는 풀이방법
input = sys.stdin.readline
hq = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        print(heapq.heappop(hq)[1] if len(hq) else 0)
    else:
        heapq.heappush(hq, (abs(x), x))
    
########### 최대, 최소 힙을 사용하는 방법 1
# input = sys.stdin.readline
# pq = []
# nq = []
# for i in range(int(input())):
#     n = int(input())

#     if (n == 0):
#         result = 0
#         rnq = 0 if len(nq)==0 else (heapq.heappop(nq))
#         rpq = 0 if len(pq)==0 else heapq.heappop(pq)

#         if(rnq == 0):
#             result = rpq
#         elif(rpq == 0):
#             result = rnq*-1
#         elif (rnq == rpq):
#             result = (rnq*-1)
#             heapq.heappush(pq, rpq)
#         else:
#             if (rnq < rpq):
#                 result = (rnq*-1)
#                 heapq.heappush(pq, rpq)
#             else:
#                 result = rpq 
#                 heapq.heappush(nq, rnq)
#         print(result)
#     else:
#         if(n>0):
#             heapq.heappush(pq,n)
#         else:
#             n = n*-1
#             heapq.heappush(nq,n)

########### 최대, 최소 힙을 사용하는 방법 2
# input = sys.stdin.readline
# min_heap = []
# max_heap = []
# for _ in range(int(input())):
#     x = int(input())
#     if x > 0 :
#         heapq.heappush(min_heap, x)
#     elif x < 0 :
#         heapq.heappush(max_heap, -x)
#     else:
#         if len(min_heap):
#             if len(max_heap) == 0 or min_heap[0] < max_heap[0]:
#                 print(heapq.heappop(min_heap))
#             else:
#                 print(-heapq.heappop(max_heap))
#         else:
#             print(-heapq.heappop(max_heap) if len(max_heap) else 0)

