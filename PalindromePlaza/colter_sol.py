from collections import Counter

n = int(input())
board = [input() for _ in range(n)]
answer = 0

def can_be_palindrome(counts):
    return all(v % 2 == 0 for v in counts.values()) or \
    bool(sum(v % 2 == 1 for v in counts.values()) == 1)

def horizontal():
    ret = 0
    for y in range(n):
        counts = Counter(board[y])
        ret += can_be_palindrome(counts)
    return ret

def vertical():
    ret = 0
    for x in range(n):
        counts = Counter([board[y][x] for y in range(n)])
        ret += can_be_palindrome(counts)
    return ret

def sweep_top_left_to_bottom_right():
    #sweep top left to bottom right
    ret = 0
    start_x = 0
    start_y = 0
    while 0 <= start_x < n and 0 <= start_y < n:
        pos_x = start_x
        pos_y = start_y
        counts = Counter()
        while 0 <= pos_x < n and 0 <= pos_y < n:
            counts[board[pos_y][pos_x]] += 1
            pos_x -= 1
            pos_y += 1
        if start_x == n - 1:
            start_y += 1
        else:
            start_x += 1
        ret += can_be_palindrome(counts)
    return ret

def sweep_bottom_left_to_top_right():
    #sweep bottom left to top right
    ret = 0
    start_x = 0
    start_y = n-1
    while 0 <= start_x < n and 0 <= start_y < n:
        pos_x = start_x
        pos_y = start_y
        counts = Counter()
        while 0 <= pos_x < n and 0 <= pos_y < n:
            counts[board[pos_y][pos_x]] += 1
            pos_x -= 1
            pos_y -= 1
        if start_x == n - 1:
            start_y -= 1
        else:
            start_x += 1
        ret += can_be_palindrome(counts)
    return ret

answer += horizontal()
answer += vertical()
answer += sweep_top_left_to_bottom_right()
answer += sweep_bottom_left_to_top_right()
print(answer)