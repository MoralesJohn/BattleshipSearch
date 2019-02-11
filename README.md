# BattleshipSearch
Searching algorithm based on the battleship board game.

Class assignment:
Given a function hit(x, y) which returns bool on a hit, write a function accepting gridSize as an argument, which searches a board containing a single ship, 3 spaces long. Return the coordinates of the ship. 

The functions are written in python 3. I have included a helper function, filter_hit_check(gridsize, x, y), which checks if the coordinates are out of bounds before submitting them to hit(x, y). Since the ship is specifically 3-spaces in length, the algorithm each line, but skips 2 spaces between checks. Upon a positive result it calls another function, find_the_rest(gridsize, x, y), which looks for the remaining ship coordinates. 
