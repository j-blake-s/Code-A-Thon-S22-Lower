#Test case generator for It's time to dddddddddddddddddddddddddddduel!
#Format:
#(a1:h1),(a2:h2),(a3:h3),(a4:h4),(a5:h5)
#(a6:h6),(a7:h7),(a8:h8),(a9:h9),(a10:h10)
#a is the monsters attack, ranging from 1 to 30
#h is the monsters health, ranging from 1 to 20
import random

if __name__ == '__main__':
    # cases = int(input())
    # for i in range(cases):
        #loop for each of the 10 cards
    board = []
    made_monster = False
    for j in range(10):
        #first we determine if a monster is in the spot, basically a coin flip
        gen = random.randrange(0,2)
        if gen == 1 or (j == 9 and not made_monster):
            #if we are making the card, generate a attack and health for it
            a = random.randrange(1,21)
            h = random.randrange(1,50) * 20
            board.append('({}:{})'.format(a,h))
            made_monster = True
        else:
            #otherwise append an empty card
            board.append('()')
    k_board = ','.join(board[0:5])
    y_board = ','.join(board[5:10])
    print(random.randint(20, 8000))
    print(k_board)
    print(y_board)

        # f = open('{}.txt'.format(i), 'w')
        # f.write(k_board)
        # f.write('\n')
        # f.write(y_board)
        # f.close()