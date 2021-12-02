import sys

def getInput(filepath = None):
        # change the extension of the file from .py to .in | split, slice (excluding the last), join + ".in"
        filepath = filepath  or ".".join(sys.argv[0].split('.')[0:-1]) + ".in"
        with open(filepath) as inFile:
            return inFile.read()

_i = [i.split() for i in getInput().splitlines()] # [(x,int(y))...]


depth = 0
forward = 0
aim = 0

for i in _i:
    val = int(i[1])
    if i[0] == "forward":
        forward += val
        depth += aim * val
    if i[0] == "up":
        # depth -= val
        aim -= val
    if i[0] == "down":
        # depth += val
        aim += val
    # print(f"{depth=} {forward=} {aim=}")


# print(f"{depth=} {forward=}")
print(depth * forward)
