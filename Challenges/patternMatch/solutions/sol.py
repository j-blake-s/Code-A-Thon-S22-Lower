#!bin/python3
n = int(input())
a = input()
# a = "abefghghighijfgCDEFiKLMNuvSTUVKLMABtacoABKLMSTUVuvKLMNiCDEFgfijghghiefghab"
pos = 0
times_removed = 0
while pos < len(a) - pos:
    if a[:pos] == a[-pos:]:
        sub = a[:pos]
        a = a.removeprefix(sub).removesuffix(sub)
        pos = 1
        # print(sub)
        # print(a)
        times_removed += 1
        continue
    pos += 1
    # print(pos)
print(a)
# print(times_removed)
assert times_removed == n