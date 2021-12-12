import sys
import pprint as pprint

def getInput(filepath = None):
        # change the extension of the file from .py to .in | split, slice (excluding the last), join + ".in"
        filepath = filepath  or ".".join(sys.argv[0].split('.')[0:-1]) + ".in"
        with open(filepath) as inFile:
            return inFile.read()


_i = getInput().splitlines()

ORDER = [int(i) for i in _i.pop(0).split(',')]

BOARDS = [] # an array of boards
for b in _i:
    if b == '':
        BOARDS.append([])
        continue
    else:
        BOARDS[-1].append([int(i) for i in b.split()])


class BingoBoard():
    def __init__(self, board) -> None:
        self.board = board; # 2d array
        self.markedLocations = []
        self.markedLocationsInverse = []
        # self.cols = [[] for _ in board[0]]
        # for i, row in enumerate(board):
        #     for ii, cell in enumerate(row):
        #         self.cols[ii].append(cell)

    def checkForMarking(self, number):
        for r in range(5):
            for c in range(5):
                if self.board[r][c] == number:
                    hasWon = self.markAndCheck([r,c]);
                    if hasWon: return True;
        return False

    def markAndCheck(self, location):
        self.markedLocations.append(location)
        self.markedLocationsInverse.append((location[1], location[0]))

        if (len(self.markedLocations) < 5): return False

        # vertical checking.
        marked = self.markedLocations.copy()
        marked.sort()

        prev_mark = marked[0];
        count = 0; # shpuld be 4 coz (its compares between 2 quantities ,so with 5 values only 4 comparisions happen (in order))
        for mark in marked[1:]:
            if mark[1] - prev_mark[1] == 1 and mark[0] == prev_mark[0]:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
            prev_mark = mark

        # for Horizontal checking
        marked = self.markedLocationsInverse.copy()
        marked.sort()

        # vertical checking.
        prev_mark = marked[0];
        count = 0; # shpuld be 4 coz (its compares between 2 quantities ,so with 5 values only 4 comparisions happen (in order))
        for mark in marked[1:]:
            if mark[1] - prev_mark[1] == 1 and mark[0] == prev_mark[0]:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
            prev_mark = mark

    def getScore(self, number):
        score = 0
        for r in range(5):
            for c in range(5):
                if [r, c] not in self.markedLocations:
                    score += self.board[r][c]
        return score * number

BOARDS = [BingoBoard(board) for board in BOARDS]

for number in ORDER:
    for bNo, board in enumerate(BOARDS, 0):
        # pprint.pprint({bNo, board})
        hasWon = board.checkForMarking(number);
        if hasWon:
            score = board.getScore(number);
            pprint.pprint(f"{bNo=} {score=}")
            exit()