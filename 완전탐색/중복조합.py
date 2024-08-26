from itertools import combinations_with_replacement

for i in combinations_with_replacement([1,2,3,4], 2):
    print(i, end=" ")
# (1, 1) (1, 2) (1, 3) (1, 4) (2, 2) (2, 3) (2, 4) (3, 3) (3, 4) (4, 4)                                                                                                              