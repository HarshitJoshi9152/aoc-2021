import sys
from pprint import pprint

def getInput(filepath = None):
#     return """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C
# """
    # change the extension of the file from .py to .in | split, slice (excluding the last), join + ".in"
    filepath = filepath  or ".".join(sys.argv[0].split('.')[0:-1]) + ".in"
    with open(filepath) as inFile:
        return inFile.read()

_i = getInput().split("\n\n")

formula = _i[0]
mappings = {}

for m in _i[1].splitlines():
    s, e = m.split(" -> ")
    mappings[s] = e

def getScore(formula):
    # or we could keep track of the count of each element in a dict incrementally
    max_s = 0
    min_s = 0xffffffffffffffff # 8 bytes so must be 1.8446744e+19
    for elm in mappings.values():
        cnt = formula.count(elm)
        if cnt > max_s:
            max_s = cnt
        if cnt < min_s:
            min_s = cnt
    return max_s - min_s

pprint(mappings)

STEPS = 10

for _ in range(STEPS):
    buffer = "xx"
    new_formula = []
    for i in formula:
        buffer += i         # add new elm
        buffer = buffer[1:] # remove last elm

        new_formula.append(i)
        elm = mappings.get(buffer)
        if elm:
            new_formula.insert(-1, elm)
    formula = "".join(new_formula)
    # print(formula)
    new_formula.clear()

print(getScore(formula))
