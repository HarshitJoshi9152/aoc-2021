import sys
from pprint import pprint

def getInput(filepath = None):
#         return """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]
# """
        # change the extension of the file from .py to .in | split, slice (excluding the last), join + ".in"
        filepath = filepath  or ".".join(sys.argv[0].split('.')[0:-1]) + ".in"
        with open(filepath) as inFile:
            return inFile.read()

_i = getInput().splitlines()
# print(_i)

closing_braces = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

syntax_error_score_table = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

syntax_error_score = 0

next_gen = []

for ln_no, line in enumerate(_i):
    stack = []
    bad = False
    for c in line:
        if c in closing_braces.values():
            if closing_braces[stack[-1]] == c:
                stack.pop()
            else:
                # print(f"error : Expected {stack[-1]} and got {c}")
                bad = True
                syntax_error_score += syntax_error_score_table[c]
                # _i.pop(ln_no);
                break;
        else:
            stack.append(c)
    if not bad:
        next_gen.append(line)
        pass

pprint(syntax_error_score)

# Part 2

autocomplete_score_table = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

scores = []

for ln_no, line in enumerate(next_gen):
    stack = []
    for c in line:
        if c in closing_braces.values():
            if closing_braces[stack[-1]] == c:
                stack.pop()
        else:
            stack.append(c)
    rest_line = ""
    line_score = 0
    while(stack):
        closing_char = closing_braces[stack[-1]]
        rest_line += closing_char
        line_score = line_score * 5 + autocomplete_score_table[closing_char]
        stack.pop()
    scores.append(line_score)

print(sorted(scores)[len(scores) // 2])