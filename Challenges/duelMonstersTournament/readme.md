 It's time to dddddddddddddddddddddddddddduel!

 I, Seto Kaiba, am the number one ranked duelist in the country, and the favorite to win the Duel Monsters championship. Hah, you wouldn't last two minutes in a duel against me. 
 
 Or, I would say that if I actually believed it anymore, Yugi has beaten me at every turn, why can't I win?! The days of Yugi defeating me are over, the Duel Monsters simulator that I have created will assure my victory!

 Given a board state, the computer will determine who will win and how many turns it will take to win, Yugi has nothing on my state of the art computer simulations.

 The computer will read in 2 sets of 5 card spaces, the first one being mine, the other being Yugi's. Each card space has 2 values, attack power and health. I go first in all games, naturally, so my monsters all attack the monster across from them, reducing their health by my attack power. If a monster's health is reduced to 0, they are destroyed, leaving that space open. If there is no monster across to attack, the monster attacks directly, dealing damage to the duelist's life points! Once my monsters attack, Yugi's pathetic monsters attack, each player starts with 20 life points and the battle continues until one of us is reduced to 0 life points. 

 The simulator is to output the winner of the current board state (K for Kaiba, Y for Yugi) and the amount of turns it takes to win (Kaiba's first turn being turn 1).

 Example:
 
 Input:

 (10:5),(),(15:3),(),()
 (4:11),(1:1),(3:16),(),()

 Output:

 K 7

 Explanation:

 Kaiba always goes first, his cards attack, dealing 10 damage to the first card on Yugi's side and 15 to the third

 (Turn 1)
 (10:5) ()    (15:3)  ()  ()    20 lp
 (4:1)  (1:1) (3:1)   ()  ()    20 lp

 Yugi's cards attack, dealing 4 to Kaiba's first monster, dealing 1 damage to Kaiba's life points, then dealing 3 damage to Kaiba's third monster, sending it to the graveyard

 (Turn 2)
 (10:4) ()    ()      ()  ()    19 lp
 (4:1)  (1:1) (3:1)   ()  ()    20 lp

 Kaiba attacks, defeating the first card

 (Turn 3)
 (10:4) ()    ()      ()  ()    19 lp
 ()     (1:1) (3:1)   ()  ()    20 lp

 Yugi attacks directly, dealing 4 damage
 
 (Turn 4)
 (10:4) ()    ()      ()  ()    15 lp
 ()     (1:1) (3:1)   ()  ()    20 lp

 Kaiba attacks directly, dealing 10 damage

 (Turn 5)
 (10:4) ()    ()      ()  ()    15 lp
 ()     (1:1) (3:1)   ()  ()    10 lp

 Yugi attacks directly, dealing 4 damage
 
 (Turn 6)
 (10:4) ()    ()      ()  ()    11 lp
 ()     (1:1) (3:1)   ()  ()    10 lp

 Kaiba attacks directly, dealing 10 damage, winning the duel

 (Turn 7)
 (10:4) ()    ()      ()  ()    11 lp
 ()     (1:1) (3:1)   ()  ()    0 lp

 Limits:

 Monster attack (a) and health (h) have a range as follows:

 0 < a <= 30
 0 < h <= 50