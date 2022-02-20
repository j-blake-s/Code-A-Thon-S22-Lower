# EOSort - Sorts an an array of random integers into ascending order, with
#     even numbers listed first, then odd odd numbers.
#
# ACM Spring '22 Code-A-Thon Lower-Division
# Inspired by Vince Kolb-Lugo
# Solved by Colter B

nums = list(map(int, input().split()))
evens = [x for x in nums if x % 2 == 0]
odds = [x for x in nums if x %2 != 0]
evens.sort()
odds.sort()
evens += odds
for n in evens:
    print(n, end=' ')