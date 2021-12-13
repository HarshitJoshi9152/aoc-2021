import sys

def getInput(filepath = None):
        #  return "16,1,2,0,4,2,7,1,2,14";
        # change the extension of the file from .py to .in | split, slice (excluding the last), join + ".in"
        filepath = filepath  or ".".join(sys.argv[0].split('.')[0:-1]) + ".in"
        with open(filepath) as inFile:
            return inFile.read()

_i = [int(i) for i in getInput().split(",")];
#  print(_i, end="")

_min = min(_i)
_max = max(_i)

def get_fuel(n):
    return (n * (n+1))//2

min_diff = 9999999999999999999999
for i in range(_min, _max+1):
    c_diff = 0
    for val in _i:
        c_diff += get_fuel(abs(val - i));
    if (abs(c_diff) < min_diff):
        #  print(f"diff = {c_diff=} & {i=}");
        min_diff = c_diff;

print(min_diff)
