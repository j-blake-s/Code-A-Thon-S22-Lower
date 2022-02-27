#!/usr/local/bin/python3
# from random import randint
import random
import string
case_num = int(input())
min_word_size = 1
max_word_size = 7
all_letters = list(string.ascii_letters)
random.seed(case_num)
random.shuffle(all_letters)
letters = "".join(all_letters) * 16
# 0 and 1 are the sample cases
if case_num == 0:
    print(2)
    print("betterplanrightplanbetter")
elif case_num == 1:
    print(5)
    print("tacoservedhotonaplateaonhotservedtaco")
else:
    # output what should be read in as input by
    # contestant code
    min_word_size = 1
    max_word_size = 7
    n = random.randint(1, 7)
    if case_num == 48:
        n = 7
        max_word_size = 1
    elif case_num >= 49:
        n = 7
        min_word_size = 7
    # j = random.randint(3, 2 ** 25)
    # temp = ([string.ascii_letters[i*(section_len:=random.randint(1,4)):(i+1)*section_len] for i in range(n)])
    temp = []
    pos = 0
    for _ in range(n):
        section_len=random.randint(min_word_size,max_word_size)
        temp.append(letters[pos:pos+section_len])
        pos+=section_len
    section_len=random.randint(min_word_size,max_word_size)
    a = "".join(temp) + letters[pos:pos+section_len] + "".join(reversed(temp))
    print(n)
    print(a)
    # print(n, j)
