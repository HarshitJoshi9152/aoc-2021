import sys
from pprint import pprint

def getInput(filepath = None):
#         return """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526
# """
        # change the extension of the file from .py to .in | split, slice (excluding the last), join + ".in"
        filepath = filepath  or ".".join(sys.argv[0].split('.')[0:-1]) + ".in"
        with open(filepath) as inFile:
            return inFile.read()

power_levels = [list(map(int, line)) for line in getInput().splitlines()]

# print(power_levels)

"""
There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus slowly
gains energy over time and flashes brightly for a moment when its energy is
full. Although your lights are off, maybe you could navigate through the cave
without disturbing the octopuses if you could predict when the flashes of light
will happen
"""

def flash(r, c):
    f_cnt = 1
    flashed_coors.append((r, c))
    power_levels[r][c] = 0

    neighbours = [  (r+1,c+1), #bottom right
                    (r+1,c-1), #bottom left
                    (r-1,c+1), #top right
                    (r-1,c-1), #top left
                    (r,c-1),  # left
                    (r-1,c),  # top
                    (r+1,c),  # down
                    (r,c+1),  # right
                 ]

    for r, c in neighbours:
        if r >= 0 and c >= 0:
            try:
                if (r, c) not in flashed_coors:
                    power_levels[r][c] += 1
                    if (power_levels[r][c] > power_lmt):
                        f_cnt += flash(r, c)
            except:
                # index doesnt exit !
                pass
    
    return f_cnt

def print_octopuses():
    for i, row in enumerate(power_levels):
        for j, power in enumerate(row):
            if (i, j) in flashed_coors:
                print(f"\x1b[91m{power}\x1b[0m", end="")
            else:
                print(f"\x1b[93m{power}\x1b[0m", end="")
        print()

flash_cnt = 0

steps_limit = 100
power_lmt = 9

flashed_coors = []

# for _ in range(steps_limit):
_ = 0
while True:
    _ += 1
    for i, row in enumerate(power_levels):
        for j, power in enumerate(row):
            if (i, j) not in flashed_coors:
                power += 1
                power_levels[i][j] = power
                if power > power_lmt:
                    flash_cnt += flash(i, j)
    # uncomment to see step by step visualisation !
    # print("step:", _ + 1)
    # print_octopuses()
    if len(flashed_coors) == 100:
        print(_) # part 2
        break;
    flashed_coors.clear()

# print(flash_cnt) # part 1