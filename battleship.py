# battleship search and destroy
# given a hit(x,y) func that returns bool
# write a func that takes a gridsize and searches for a 3-unit ship

def hit(x, y):
    if y == 3 and x in [3, 4, 2]:
        return True
    return False

def cruiser_search(gridsize):
    for x in range(1, gridsize + 1):
        indent = (x % 3) + 1
        for y in range(indent, gridsize + 1, 3):
            if hit(x, y):
                return find_the_rest(gridsize, x, y)
    return []

def find_the_rest(gridsize, x, y):
    center = (x, y)
    left = (x - 1, y)
    left_check = filter_hit_check(gridsize, left[0], left[1])
    right = (x + 1, y)
    right_check = filter_hit_check(gridsize, right[0], right[1])
    if left_check or right_check:
        if left_check:
            return [left, center, right] if right else [(x-2, y), left, center]
        return [center, right, (x + 2, y)]
    up = (x, y-1)
    up_check = filter_hit_check(gridsize, up[0], up[1])
    down = (x, y+1)
    down_check = filter_hit_check(gridsize, down[0], down[1])
    if up_check:
        return [up, center, down] if down_check else [(x, y-2), up, center]
    return [center, down, (x, y + 2)]

def filter_hit_check(gridsize, x, y):
    legal = range(1, gridsize + 2)
    if x in legal and y in legal:
        return hit(x, y)
    return False

print(cruiser_search(10))
