import sys
from pprint import pprint

def getInput(filepath = None):
#     return """6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5"""
    # change the extension of the file from .py to .in | split, slice (excluding the last), join + ".in"
    filepath = filepath  or ".".join(sys.argv[0].split('.')[0:-1]) + ".in"
    with open(filepath) as inFile:
        return inFile.read()

_i = getInput().split("\n\n")

points = list(map(lambda x: tuple(map(int, x.split(","))) ,_i[0].splitlines()))


# we need to fold the coors on the other side of the line !
def fold(pt, line_y = 0, line_x = 0):
    """
       0 1 2 3
    0  . . # .
    1  . # . .
    2  . . . .
    3  . # . .
    4  . . # .

    say we fold at y = 2:           obs: the changed part of coors is the line point given in arg.
    (x=1, y=3) becomes (x=1, y=1) | take distance from `y = 2` and subtract of distance to `y` (foldpoint)
    (x=2, y=4) becomes (x=1, y=0)
    """
    # y, x = (pt['y'], pt['x'])
    x, y = pt
    # 1 as dist means the point will lay on the line right ?
    if line_y:
        dist = y - line_y # distance from division pt
        # print(line_y - dist)
        # if pt == [6, 10]:
        #     print(f"line_y, dist {line_y} {dist}")
        #     print(f"(line_y - dist) f{(line_y - dist)}")
        return (x, line_y - dist) if (line_y - dist) >= 0 else "Out Of Range !"
    elif line_x:
        dist = x - line_x # distance from division pt
        # print(line_x - dist)
        return (line_x - dist, y) if (line_x - dist) >= 0 else "Out Of Range !"
    else:
        raise Exception("No Line point provided for folding !")

# print(fold({'y':4, 'x':2}, line_y=2))

foldings = []

# parsing folding insts
for ln in _i[1].splitlines():
    xy, pt = ln.split("=")
    xy = xy[-1]
    pt = int(pt)
    if xy == "y":
        # foldings.append({'y':pt, 'x': 0})
        foldings.append({'y':pt})
    elif xy == "x":
        # foldings.append({'x':pt, 'y': 0})
        foldings.append({'x':pt})

def graph_pts(points):
    max_x = 0
    max_y = 0
    for pt in points:
        x, y = pt
        if x > max_x:
            max_x = x
        elif y > max_y:
            max_y = y

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            # print([x, y], [x, y] in points, end="")
            if (x, y) in points:
                print("#", end="")
            else:
                print(".", end="")
        print("")

pts_new = set()
for fold_inst in foldings:
    # folding all the points according to the folding instructions
    if fold_inst.get('x'):
        fold_pt = fold_inst['x']
        for pt in list(points):
            if pt[0] > fold_pt:
                folded_pt = fold(pt, line_x=fold_pt)
                if type(folded_pt) == tuple:
                    pts_new.add(folded_pt)
                # print(f"Folded {pt} -> {folded_pt} on y axis")
            else:
                pts_new.add(tuple(pt))
    elif fold_inst.get('y'):
        fold_pt = fold_inst['y']
        for pt in list(points):
            if pt[1] > fold_pt:
                folded_pt = fold(pt, line_y=fold_pt)
                if type(folded_pt) == tuple:
                    pts_new.add(folded_pt)
                # print(f"Folded {pt} -> {folded_pt} on y axis")
            else:
                pts_new.add(tuple(pt))
    # graph_pts(list(points))
    points = pts_new
    pts_new = set()

print(len(points))
graph_pts(list(points))
