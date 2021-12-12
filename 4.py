import sys
import pprint as pprint

def getInput(filepath = None):
#         return """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7"""
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


for bingoNumber in ORDER:
    bNo = 0
    while bNo < len(BOARDS):
        board = BOARDS[bNo]
        # pprint.pprint({bNo, board})
        hasWon = board.checkForMarking(bingoNumber);
        if hasWon:
            score = board.getScore(bingoNumber);
            pprint.pprint(f"{bNo=} {score=} {bingoNumber=} ")
            BOARDS.pop(bNo);
        else:
            bNo += 1