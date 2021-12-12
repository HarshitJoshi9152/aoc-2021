import sys

def getInput(filepath = None):
    # change the extension of the file from .py to .in | split, slice (excluding the last), join + ".in"
    filepath = filepath  or ".".join(sys.argv[0].split('.')[0:-1]) + ".in"
    with open(filepath) as inFile:
        return inFile.read()

_i = getInput().splitlines()

gamma_rate = ""
nums = len(_i)
num_len = range(len(_i[0]))

for index in num_len:
    count = 0
    for i in _i:
        if i[index] == '0':
            count += 1

    gamma_rate += '1' if (nums - count > count) else '0';

def bin_not(n):
    return "".join(['1' if (i == '0') else '0' for i in n])

epsion_rate = int(bin_not(gamma_rate), 2)
gamma_rate = int(gamma_rate, 2)

# part 1 solution
print(gamma_rate * epsion_rate)


# part 2
q1 = 0;
q2 = 0;

# getCommonList relies on buffer_lst to narrow down to 1 number (it needs to mutate it)
buffer_lst = _i.copy()

def getCommonList(index, reverse = False):
    # defaults to oxygen generator rating
    count_0 = 0
    list_0 = []
    count_1 = 0
    list_1 = []

    for i in buffer_lst:
        if (i[index] == '0'):
            count_0 += 1
            list_0.append(i)
        else:
            count_1 += 1
            list_1.append(i)

    if (count_0 > count_1):
        return list_0 if (reverse == False) else list_1
    elif (count_0 == count_1):
        # OXYGEN REV=FALSE
        # If 0 and 1 are equally common, keep values with a 1 in the position being considered.
        return list_1 if (reverse == False) else list_0
    else:
        return list_1 if (reverse == False) else list_0

# finding Q1 : oxygen rating
for index in num_len:
    lst = getCommonList(index);
    if len(lst) == 1:
        q1 = lst[0]
        break;
    else:
        buffer_lst = lst
        continue;

buffer_lst = _i.copy();

# finding Q1 : carbon rating
for index in num_len:
    lst = getCommonList(index, True);
    if len(lst) == 1:
        q2 = lst[0]
        break;
    else:
        buffer_lst = lst
        continue;

q1 = int(q1, 2)
q2 = int(q2, 2)
print(q1 * q2)
"""
Next, you should verify the life support rating, which can be determined by
multiplying the oxygen generator rating by the CO2 scrubber rating.
"""
