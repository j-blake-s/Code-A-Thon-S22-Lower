#!/usr/local/bin python3

# read input
N = int(input())
P = [[int(o) for o in input().split()] for i in range(N)]
# to store the solution set
sols = [0 for i in range(N)]

# analyze input
for i in range(N):
    for j in range(N):
        # find the missing entries
        if P[i][j] == 0:
            # find what was missing here
            t = max(i,j) - min(i,j) + 1
            # store it in sorted (left-right) order
            sols[j] = t

# print formatted input
print(' '.join([str(o) for o in sols]))
