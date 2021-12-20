import sys
from pprint import pprint

def getInput(filepath = None):
#     return """fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW
# """
#     return """dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc
# """
#     return """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end
# """
    # change the extension of the file from .py to .in | split, slice (excluding the last), join + ".in"
    filepath = filepath  or ".".join(sys.argv[0].split('.')[0:-1]) + ".in"
    with open(filepath) as inFile:
        return inFile.read()

_i = getInput().splitlines()

graph = {}

# make the data structure

for line in _i:
    start, end = tuple(line.split("-"));
    if graph.get(start):
        graph[start].append(end)
    else:
        graph[start] = [end]
    # it goes both ways
    if graph.get(end):
        graph[end].append(start)
    else:
        graph[end] = [start]

# pprint(graph)
# print()

# {'A': ['c', 'b', 'end'], 'b': ['d', 'end'], 'start': ['A', 'b']}


paths = []

def solve(pos, path = [], visited = set()):
    path.append(pos)
    if pos.islower():
        visited.add(pos)
    for next_pos in graph[pos]:
        if next_pos == "end":
            paths.append(path+["end"])
            continue
        if next_pos not in visited and graph.get(next_pos) and next_pos != "start":
            solve(next_pos, path.copy(), visited.copy())

res = solve("start")

def print_path(path):
    for p in path[0:-1]:
        print(p, end=" -> ")
    print(path[-1])

# [print_path(p) for p in paths]

print(len(paths))