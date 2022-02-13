Given a square character matrix, count how many columns, rows, and diagonals can possibly make a palindrome.

Note that we are not counting the number of palindromes, just if they can be made into one.

Note: we consider a single character as a palindrome.


Example 1:


a b a
d c d
a b a

Returns 12, 3 rows, 3 cols, 3 diagonal from top right to top left, 3 from 
diagonal top left to top right.

in order:

(aba),(dcd),(aba),
(ada),(bcb),(ada),
(a),(aca),(a)
(a),(aca),(a)

Data is written row by row, ie the above example would be

aba
dcd
aba

Example 2:

a b b a
b a c d
b a d c
a b d d

Returns 13, 
Listing the matches:
rows:
(abba) (bdd): 2
columns:
(abba) : 1
diagonal top left to bottom right:
(a),(bb),(bab),(bdd), (d) : 5
diagonal top right to bottom left:
(a),(bcc),(aadd),(bb),(a) : 5

Summing all yields 13. Again, note that we include items like (bdd) because it CAN
be made into a palindrome (dbd); it itself need not already be a palindrome.