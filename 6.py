import sys

def getInput(filepath = None):
        # return "3,4,3,1,2"
        # return "3,4,3,1,2"
        # change the extension of the file from .py to .in | split, slice (excluding the last), join + ".in"
        filepath = filepath  or ".".join(sys.argv[0].split('.')[0:-1]) + ".in"
        with open(filepath) as inFile:
            return inFile.read()

_i = getInput()

# part 1
fishes = list(map(int, _i.split(",")))

dayslimit = 80
day = 0;
# fishes_producted_by = []
while day < dayslimit:
    next_gen = []
    # for fish in fishes:
    for fi, fish in enumerate(fishes):
        if fish == 0:
            next_gen.append(6);
            # if len(fishes_producted_by) > fi and fishes_producted_by[fi]:
            #     fishes_producted_by[fi] += 1
            # else:
            #     fishes_producted_by[fi] = 1
            next_gen.append(8);
        else:
            next_gen.append(fish - 1)
    fishes = next_gen
    # print(fishes)
    day += 1

print(len(fishes))


# part 2

# like tsoding index is the no of days (the timer) and the value is the no of fishes having that timer
fishes_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in list(map(int, _i.split(","))):
    fishes_list[i] += 1

fishes_buffer = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def sim_day():
    global fishes_list, fishes_buffer
    fishes_buffer[6] += fishes_list[0]
    fishes_buffer[8] += fishes_list[0]

    for index in range(1, 9):    # already evaluated index 0
        fishes_buffer[index - 1] += fishes_list[index]

    fishes_list = fishes_buffer.copy()
    fishes_buffer = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(256):
    # print(f"{fishes_list=}")
    sim_day()
    # print(f"{fishes_list=}")

print(sum(fishes_list))



"""

# we are not reseting this fish again, wait we dont need to wtf am i thinking  !!
def calc_fish(fish_stage, days_left):
    if (days_left < (fish_stage + 1)): return 0

    days_left = days_left - (fish_stage + 1)
    # print(f"fist {days_left=}")
    offsprings = 1

    offsprings += days_left // 7 # 7 days are required
    # print(f"{days_left=} // 7 = {days_left // 7}")

    for offspring in range(0, offsprings):
        days_left = days_left - 7 * offspring
        if (days_left > 0):
            offsprings += calc_fish(8, days_left)

    return offsprings;

# 3,4,3,1,2
print(calc_fish(3, dayslimit))
# print(calc_fish(3, 80) + calc_fish(4, 80) + calc_fish(3, 80) + calc_fish(1, 80) + calc_fish(2, 80))


# 3 , 80

# daysleft after fish2 = 80 - (3 + 1) = 76

# 76 // 7 = 10

# 1_st fish => 8, 76 - (7 * 1) calc(8, 69)


"""