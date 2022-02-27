# It's time to dddddddddddddddddddddddddddduel! Solver
# Nothing too complicated, naive approach should be fine
# Only tricky part here is parsing and getting the lists set up

def parse_board(board):
    attack_list = []
    health_list = []

    board_split = board.split(',')

    board_split = [x.strip()[1:-1] for x in board_split]

    for card in board_split:
        if card == '':
            attack_list.append(0)
            health_list.append(0)
            continue
        attack_health = card.split(':')
        attack_list.append(int(attack_health[0]))
        health_list.append(int(attack_health[1]))
    
    return attack_list, health_list

if __name__ == '__main__':
    start_lp = int(input())
    k_board = input()
    y_board = input()

    k_attack, k_health = parse_board(k_board)
    y_attack, y_health = parse_board(y_board)

    turn = 0

    k_lp = start_lp
    y_lp = start_lp

    while k_lp > 0 and y_lp > 0:
        if turn % 2 == 0:
            #Kaiba's turn
            for i in range(len(k_attack)):
                if k_health[i] > 0:
                    if y_health[i] > 0:
                        y_health[i] -= k_attack[i]
                    else:
                        y_lp -= k_attack[i]
        else:
            #Yugi's turn
            for i in range(len(y_attack)):
                if y_health[i] > 0:
                    if k_health[i] > 0:
                        k_health[i] -= y_attack[i]
                    else:
                        k_lp -= y_attack[i]
        turn += 1

print('K' if k_lp > 0 else 'Y', str(turn))