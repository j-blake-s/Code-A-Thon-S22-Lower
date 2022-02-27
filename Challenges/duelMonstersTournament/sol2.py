'''
(10:5),(),(15:3),(),()
(4:11),(1:1),(3:16),(),()
'''
empty = "_"

class Monster:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health
    def __repr__(self):
        return f"({self.attack}, {self.health})"

def parse():
    line = input().split(",")
    for i in range(len(line)):
        if line[i] != "()":
            a, h = map(int, line[i][1:-1].split(":"))
            line[i] = Monster(a, h)
        else:
            line[i] = empty
    return line


start_lp = int(input())
k_monsters = parse()
y_monsters = parse()

k_lp = start_lp
y_lp = start_lp
turn_num = 0
while k_lp > 0 and y_lp > 0:
    turn_num += 1
    for col in range(5):
        if turn_num % 2 == 1:
            if k_monsters[col] == empty:
                continue
            #we have a monster, but yugi does not
            if y_monsters[col] == empty:
                y_lp -= k_monsters[col].attack
            else:
                y_monsters[col].health -= k_monsters[col].attack
                if y_monsters[col].health <= 0:
                    y_monsters[col] = empty
        else:
            if y_monsters[col] == empty:
                continue
            #yugi has a monster, but kaiba does not
            if k_monsters[col] == empty:
                k_lp -= y_monsters[col].attack
            else:
                k_monsters[col].health -= y_monsters[col].attack
                if k_monsters[col].health <= 0:
                    k_monsters[col] = empty
    # print(k_lp, y_lp)
    # print(k_monsters)
    # print(y_monsters)
    # print("=========")


print("K" if k_lp > 0 else "Y", turn_num)

