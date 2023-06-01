Noughts and Crosses v2.0

by Sam D Parsons

The old game of noughts and crosses (British English), or Tic-tac-toe (American English), programmed in Python using Pygame library. 

A 3x3 matrix represents the board. Each player is assigned a value of positive one and negative one respectively. Empty squares are given a value of zero.

A starting board would look like this:

[ 0  0  0 ]
[ 0  0  0 ]
[ 0  0  0 ]

A diagonal win for player (1) would look like this:

[ 1  0 -1 ]
[ 0  1  0 ]
[-1  0  1 ]

The winning condition was solved using 3x3 matrix and by finding the sum of every, row, column, and both diagonals. A win would result in sum of either 3 or -3. Draw condition was defined as number of moves = 9 and no win condition (i.e. no row, column, diagnoal sum to -3).

TODO:

Implement AI. Currently the computer goes in the first available space on the board.