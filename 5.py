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

# pprint(points_map)

# ground starts at 0,0 and ends at 9,9 so size = 10 by 10 | ONLY FOR EXAMPLE
buffer_size = 1000
buffer = [[*('.'*buffer_size)] for _ in range(buffer_size)]
counted_points = []

def get_range(val1, val2):
    if val1 < val2:
        return range(val1, val2 + 1)
    else:
        return range(val2, val1 + 1)

danger_count = 0 # the number of points where at least two lines overlap

for start_pt, end_pt in points_map:
    # if not (start_pt[0] == end_pt[0] or start_pt[1] == end_pt[1]):
    #     continue;
    if start_pt[0] == end_pt[0]:
        # print((start_pt, end_pt)) # REMOVE ME
        # x is same so vertical line
        x_coor = start_pt[0];
        for y_coor in get_range(start_pt[1], end_pt[1]):
            # the value at the coor before
            val = buffer[y_coor][x_coor]
            # new value for the coor
            buffer[y_coor][x_coor] = str(int(val) + 1) if val != '.' else "1"
            if ([y_coor, x_coor] not in counted_points) and int(buffer[y_coor][x_coor]) > 1:
                counted_points.append([y_coor, x_coor])
                danger_count += 1

    elif start_pt[1] == end_pt[1]:
        # print((start_pt, end_pt)) # REMOVE ME
        # y is same so horizontal line
        y_coor = start_pt[1];
        for x_coor in get_range(start_pt[0], end_pt[0]):
            # the value at the coor before
            val = buffer[y_coor][x_coor]
            # new value for the coor
            buffer[y_coor][x_coor] = str(int(val) + 1) if val != '.' else "1"
            if ([y_coor, x_coor] not in counted_points) and int(buffer[y_coor][x_coor]) > 1:
                counted_points.append([y_coor, x_coor])
                danger_count += 1
    else:
        # print((start_pt, end_pt))
        pass

# pprint(buffer)
print(danger_count)
