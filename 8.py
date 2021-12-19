import sys
from pprint import pprint
def getInput(filepath = None):
#         return """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
# """
        # change the extension of the file from .py to .in | split, slice (excluding the last), join + ".in"
        filepath = filepath  or ".".join(sys.argv[0].split('.')[0:-1]) + ".in"
        with open(filepath) as inFile:
            return inFile.read()

_i = [x.split('|') for x in getInput().splitlines()]

count = 0

for output in [i[1].split() for i in _i]:
    for digit in output:
        if len(digit) in [2, 4, 3, 7]:
            count += 1
print(count)

# part 2 took me like 2 hours ig. Nighttime is nto a good time to do a lot of thinking when yu are tired
def findMatches(seqs, output):
    seq_map = {} # contains the sequences in list by index of their lengths 
    for s in seqs:
        if seq_map.get(len(s)):
            seq_map[len(s)] += [s]
        else:
            seq_map[len(s)] = [s]

    digits = {};
    characters = {
        "a":None,
        "b":None,
        "c":None,
        "d":None,
        "e":None,
        "f":None,
        "g":None,
    }
    # step 1 Determine 1, 4, 7, 8
    for seq in seqs:
        l = len(seq)
        if l == 2:
            digits[1] = set(seq)
        if l == 4:
            digits[4] = set(seq)
        if l == 3:
            digits[7] = set(seq)
        if l == 7:
            digits[8] = set(seq)

    characters['a'] = digits[7] - digits[1]

    # find digits 2, 3 and 5
    for seq in seq_map[5]:
        s = set(seq)
        l = len(seq)
        r = (s - digits[4]) - characters['a']
        if len(r) == 1:
            characters['g'] = r
        else:
            digits[2] = s;
            for seq_i in seq_map[5]:
                sq = set(seq_i)
                l = len(list(sq - s))
                if l == 1:
                    digits[3] = sq
                if l == 2:
                    digits[5] = sq

    characters["d"] = set.intersection(*[set(s) for s in seq_map[5]], digits[4])

    for seq in seq_map[6]:
        seq = set(seq)
        if seq - characters["d"] == seq:
            digits[0] = seq


    for seq in seq_map[6]:
        seq = set(seq)
        if seq == digits[0]: continue
        rp = (digits[8] - seq) & digits[1]
        if rp:
            digits[6] = seq
        else:
            digits[9] = seq


    result = ""
    for i in output:
        match = set(i)
        for key, val in zip(digits.keys(), digits.values()):
            if val == match:
                result += str(key)

    return int(result)

s = 0
for i in _i:
    seq, out = i;
    s += findMatches(seq.split(), out.split())
print(s)