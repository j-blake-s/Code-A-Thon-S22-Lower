import re
n = int(input())
a = input()
pat =  r"(.{1,7}?)" * n + r"(.{1,7})" + r"".join(f"\\{i}" for i in range(n, 0, -1)) 
print(re.fullmatch(pat, a).groups()[-1])
