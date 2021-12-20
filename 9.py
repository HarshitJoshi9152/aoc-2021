import sys

def getInput(filepath = None):
#         return """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# """
        # change the extension of the file from .py to .in | split, slice (excluding the last), join + ".in"
        filepath = filepath  or ".".join(sys.argv[0].split('.')[0:-1]) + ".in"
        with open(filepath) as inFile:
            return inFile.read()

height_map = getInput().splitlines()
# print(_i)

def is_lowest(val, val_r, val_c):
    for r, c in [(val_r+1, val_c), (val_r, val_c+1), (val_r-1, val_c), (val_r, val_c-1)]:
        if r < 0 or c < 0:
            continue
        try:
            if int(height_map[r][c]) <= val:
                return False
        except:
            continue
    return True

lowest_pts = []
lowest_pts_indexes = []

for r, i in enumerate(height_map):
    for c, val in enumerate(i):
        if is_lowest(int(val), r, c):
            lowest_pts.append(int(val))
            lowest_pts_indexes.append((r,c))

print("Part 1:", sum(lowest_pts) + len(lowest_pts))
# val='9' r=2 c=54 | avoid

basin_indexes=[]

def get_basin(pt):
    val_r, val_c = pt;
    val = int(height_map[val_r][val_c])
    ct = 1
    for r, c in [(val_r+1, val_c), (val_r, val_c+1), (val_r-1, val_c), (val_r, val_c-1)]:
        if r < 0 or c < 0:
            continue
        try:
            cell_val = int(height_map[r][c])
            if (r, c) not in basin_indexes and cell_val != 9 and (cell_val - val) >= 1:
                basin_indexes.append((r,c))
                ct += get_basin((r, c))
            else:
                continue
        except:
            continue
    return ct

basin_depths = []

# finding basins
for pt in lowest_pts_indexes:
    r, c = pt
    depth = get_basin((r,c))
    basin_depths.append(depth)

top_3_basins = sorted(basin_depths)[-3:]

print("Part 2:", top_3_basins[0] * top_3_basins[1] * top_3_basins[2])

def print_height_map():
    for r_index, r in enumerate(height_map):
        for c_index, c in enumerate(r):
            if (r_index, c_index) in lowest_pts_indexes:
                print(f"\x1b[91m{c}\x1b[0m", end="")
            elif (r_index, c_index) in basin_indexes:
                print(f"\x1b[36m{c}\x1b[0m", end="")
            else:
                print(c, end="")
        print("")

# print_height_map()