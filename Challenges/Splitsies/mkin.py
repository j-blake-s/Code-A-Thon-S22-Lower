#!/usr/local/bin/python3
import random
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print(5)
    print(12, 7, 8, 4, 5)
elif case_num == 1:
    print(4)
    print(2, 99, 4, -4)
else:
    # output what should be read in as input by
    # contestant code

    n = case_num*500 if case_num > 25 else random.randint(3, 10)
    print(n)
    nums = [random.randint(-500, 500) for _ in range(n)]
    print(*nums)
    # j = randint(3, 2 ** 25)
    # print(n, j)
