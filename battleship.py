# battleship search and destroy
# given a hit(x,y) func that returns bool
# write a func that takes a gridsize and searches for a 3-unit ship

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
