from itertools import permutations
state = '123456780'

index_state = [''.join(p) for p in permutations(state)]
state_index = {}

for index in range(len(index_state)):
    state_index[index_state[index]] = index


def get_state(index):
    return index_state[index]


def get_index(state):
    return state_index[state]


def get_children(index=None, state=None):
    if index == None:
        s = state
    else:
        s = get_state(index)

    i = s.find('0')
    if i == 0:
        return [get_index(swap(s, i, i + 1)), get_index(swap(s, i, i + 3))]
    elif i <= 2:
        return [get_index(swap(s, i - 1, i)), get_index(swap(s, i, i + 1)), get_index(swap(s, i, i + 3))]
    elif i == 8:
        return [get_index(swap(s, i - 3, i)), get_index(swap(s, i - 1, i))]
    elif i >= 6:
        return [get_index(swap(s, i - 3, i)), get_index(swap(s, i - 1, i)), get_index(swap(s, i, i + 1))]
    else:
        return [get_index(swap(s, i - 3, i)), get_index(swap(s, i - 1, i)), get_index(swap(s, i, i + 1)), get_index(swap(s, i, i + 3))]


def swap( s, i1, i2):
    return s[0:i1]+s[i2]+s[i1+1:i2]+s[i1]+s[i2+1:]


def is_goal(index):
    if state == get_state(index):
        return True
    return False


def solve(algorithm, root, has_path=False, should_reverse=True):
    par = algorithm(start=root)

    if len(par) == 0:
        print("Not found")
        return

    if not has_path:
        current = 0
        path = [current]
        while par[current] != -1:
            path.append(par[current])
            current = par[current]
    else:
        path = par
    if should_reverse:
        path.reverse()
    for p in path:
        printer(index=p)


def printer(index = None, state = None):
    if index == None:
        s = state
    else:
        s = get_state(index)
    ss = [char for char in s]
    out = ''
    ii = 0
    for i in ss:
        out += i+' '
        ii += 1
        if ii == 3:
            print(f'| {out}|')
            ii = 0
            out = ''
    print()


def get_input():
    f = open('input.txt','r')
    input = ''
    for n in range(3):
        r = f.readline()[:-1].split(' ')
        for i in r:
            input += i
    return get_index(input)


def get_manhatan_heuristic(index):
    s = get_state(index)

    def get_manhatan(index, value):
        if value == 0:
            return abs(2 - int(index / 3)) + abs(2 - (index % 3))
        else:
            return abs(int(index / 3) - int((value - 1) / 3)) + abs((index % 3) - ((value - 1) % 3))

    sum = 0
    for i in range(len(s)):
        sum += get_manhatan(i, int(s[i]))
    return sum
