import sys
from pprint import pprint

def getInput(filepath = None):
#         return """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2"""
        # change the extension of the file from .py to .in | split, slice (excluding the last), join + ".in"
        filepath = filepath  or ".".join(sys.argv[0].split('.')[0:-1]) + ".in"
        with open(filepath) as inFile:
            return inFile.read()

_i = [i.split(" -> ") for i in getInput().splitlines()]

lines_coors = _i
points_map = []

for points in lines_coors:
    ps = [[int(p) for p in points[0].split(',')], [int(p) for p in points[1].split(',')]]
    points_map.append(ps)


buffer = {}

def get_range(val1, val2):
    if val1 < val2:
        return range(val1, val2 + 1)
    else:
        return range(val2, val1 + 1)

def is_diag(start_pt, end_pt):
    pts = [start_pt, end_pt]
    pts.sort()          # sorts them in increasing order giving us the smaller value
    start_pt, end_pt = pts;

    start_x, start_y = start_pt
    end_x, end_y = end_pt

    return (abs(end_x - start_x) == abs(end_y - start_y))

def get_diag_range(start_pt, end_pt):
    pts = [start_pt, end_pt]
    pts.sort()          # sorts them in increasing order giving us the smaller value
    [start_x, start_y], [end_x, end_y] = pts;

    lst = [] # range points list
    # these ranges assure the motion (points increment) is from left->right and top->bottom
    y_range = range(start_y, end_y + 1)
    x_range = range(start_x, end_x + 1)

    # to invert y-range if required like for [[8,0], [0,8]]
    if ((end_y +1) - start_y < 0):
        y_range = range(start_y, end_y - 1, -1)

    # to invert x-range if required
    if ((end_x +1) - start_x < 0):
        x_range = range(start_x, end_x - 1, -1)


    for x, y in zip(x_range, y_range):
        lst.append([x,y])
    return lst

for start_pt, end_pt in points_map:
    if start_pt[0] == end_pt[0]:
        # x is same so vertical line
        x_coor = start_pt[0];
        for y_coor in get_range(start_pt[1], end_pt[1]):
            pt_repr = f"{y_coor} {x_coor}"
            val = buffer.get(pt_repr, None)
            buffer[pt_repr] = buffer[pt_repr] + 1 if (val) else 1

    elif start_pt[1] == end_pt[1]:
        # print((start_pt, end_pt)) # REMOVE ME
        # y is same so horizontal line
        y_coor = start_pt[1];
        for x_coor in get_range(start_pt[0], end_pt[0]):
            pt_repr = f"{y_coor} {x_coor}"
            val = buffer.get(pt_repr, None)
            buffer[pt_repr] = buffer[pt_repr] + 1 if (val) else 1

    elif is_diag(start_pt, end_pt):
        # print(start_pt, end_pt);
        pts_range = get_diag_range(start_pt, end_pt)
        for pt in pts_range:
            pt_repr = f"{pt[1]} {pt[0]}"
            val = buffer.get(pt_repr, None)
            buffer[pt_repr] = buffer[pt_repr] + 1 if (val) else 1
    else:
        pass

pprint(len([i for i in buffer.values() if int(i) >= 2]))
