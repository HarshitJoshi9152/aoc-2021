import sys
from pprint import pprint

# from collections import Counter
from string import ascii_uppercase

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

STEPS = 10

# Part 1 solution
for _ in range(STEPS):
    buffer = "aa"
    new_formula = []
    for i in formula:
        buffer += i
        buffer = buffer[1:]
        new_formula.append(i)
        elm = mappings.get(buffer)
        if elm:
            new_formula.insert(-1, elm)
    formula = "".join(new_formula)
    # print(formula)

print(getScore(formula))

# PART 2 :
# to solve this i had to watch a writeup on youtube 
# the guy suggested frequency analysis and we have already
# used frequency analysis once this year so i guess i 
# understand some frequency analysis now ! awesome

STEPS = 40
pairs = ["".join(i) for i in zip(_i[0], _i[0][1:])]

count_obj = dict.fromkeys(mappings.keys(), 0)
# setting up the object for use
for p in pairs:
    count_obj[p]+=1

# pprint(count_obj)

for _ in range(STEPS):
    new_count_obj = dict.fromkeys(mappings.keys(), 0)
    for pair, count in count_obj.items():
        # pprint((pair, count))
        if count < 0:
            continue
        new_elm = mappings[pair]
        new_count_obj[pair[0] + new_elm] += count
        new_count_obj[new_elm + pair[1]] += count
    count_obj = new_count_obj.copy()


def score(obj):
    elm_freq = dict.fromkeys(ascii_uppercase, 0)
    for k, v in obj.items():
        elm1, elm2 = (k[0], k[1])
        # print(elm1, elm2, v)
        elm_freq[elm1] += v
        elm_freq[elm2] += v

    # print(elm_freq)

    elm_freq[_i[0][0]] += 1     # first_elm_from_formula
    elm_freq[_i[0][-1]] += 1    # last_elm_from_formula

    count_list = [X // 2 for X in elm_freq.values() if X > 0]

    return max(count_list) - min(count_list)


print(score(count_obj))