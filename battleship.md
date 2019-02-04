### X419-01: Take-Home Assignment 1 -- John Morales
Assume you are given a function bool hit(int x,int y) that returns true 
if there was a hit to a ship and false if not. You are to write a 
function that returns the coordinates of a single ship on a grid of given 
size, the function takes at least one argument int gridSize and must return 
the coordinates of the 3 unit ship present in the board in the shortest 
time possible. Estimate the Time and memory complexity of your proposed 
solution. You are to select the data structure to return what you need as 
output and the prototype of the function.

### Answer: 
```
def cruiser_search(gridsize):
    for x in range(1, gridsize + 1):
        indent = (x % 3) + 1
        for y in range(indent, gridsize + 1, 3):
            if hit(x, y):
                return find_the_rest(gridsize, x, y)
    return []

def find_the_rest(gridsize, x, y):
    center = (x, y)
    left = filter_hit_check(gridsize, x - 1, y)
    right = filter_hit_check(gridsize, x + 1, y)
    if left or right:
        if left:
            return [left, center, right] if right else [(x-2, y), left center]
        return [center, right, (x + 2, y)]
    up = filter_hit_check(gridsize, x, y - 1)
    down = filter_hit_check(gridsize, x, y + 1)
    if up:
        return [up, center, down] if down else [(x, y-2), up, center]
    return [center, down, (x, y + 2)]

def filter_hit_check(gridsize, x, y):
    legal = range(1, gridsize + 2)
    if x in legal and y in legal:
        return hit(x, y)
    return False

```

I am assuming the grid is numbered from 1 to gridSize. I am not assuming
that the hit function will gracefully return false with out-of-bounds 
coordinates, so I am writing a helper function to check for that. 

I am looping on an array of 1 to gridSize, inclusive. Inside that, I am 
looping an array of (gridSize/3) -- starting at 1, 2 or 3 and maxing out
at gridSize in increments of 3. The resulting time complexity is N * N/3 
or O(n^2). The arrays for the inner loop is instantiated one at a time 
and destroyed on each outer loop increment, so the resulting space
complexity is N + N/3 or O(n).
