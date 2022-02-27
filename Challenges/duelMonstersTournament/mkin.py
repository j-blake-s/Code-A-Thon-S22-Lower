#!/usr/local/bin/python3
import random
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print(4, 2)
elif case_num == 1:
    print(5, 4)
else:
    # output what should be read in as input by
    # contestant code
    n = random.randint(3, 100000)
    j = random.randint(3, 2 ** 25)
    print(n, j)
