import copy


def create_swamps(size_swamp):
    left = size_swamp // 2 * '>'
    right = size_swamp // 2 * '<'

    left_frogs = [i for i in left]
    right_frogs = [i for i in right]

    start = left_frogs + ['_'] + right_frogs
    end = right_frogs + ['_'] + left_frogs

    return start, end


def solver(size_swamp):
    start_swamp, end_swamp = create_swamps(size_swamp)

    solved = check_possibilites(start_swamp, end_swamp)

    for step in solved:
        print(step)


def check_possibilites(swamp, end_swamp):
    queue = []
    directions = [left, left2, right, right2]

    queue.append([swamp])

    while queue:
        new = []
        path = queue.pop()
        node = path[-1]

        if node == end_swamp:
            return path

        for way in directions:
            temp = copy.deepcopy(node)
            pad_pos = temp.index('_')
            res = way(temp, pad_pos)

            if res is not None:
                new.append(res)

        for val in new:
            comb = path + [val]
            queue.append(comb)


def left(temp, pad_pos):
    if temp[pad_pos - 1] == '>' and (pad_pos - 1) > -1:
        temp[pad_pos] = temp[pad_pos - 1]
        temp[pad_pos - 1] = '_'
        return temp


def left2(temp, pad_pos):
    if temp[pad_pos - 2] == '>' and (pad_pos - 2) > -1:
        temp[pad_pos] = temp[pad_pos - 2]
        temp[pad_pos - 2] = '_'
        return temp


def right(temp, pad_pos):
    if (pad_pos + 1) <= len(temp) - 1:
        if temp[pad_pos + 1] == '<':
            temp[pad_pos] = temp[pad_pos + 1]
            temp[pad_pos + 1] = '_'
            return temp


def right2(temp, pad_pos):
    if (pad_pos + 2) <= len(temp) - 1:
        if temp[pad_pos + 2] == '<':
            temp[pad_pos] = temp[pad_pos + 2]
            temp[pad_pos + 2] = '_'
            return temp


def main():
    size_swamp = int(input("Enter number of pads: "))

    solver(size_swamp)


if __name__ == '__main__':
    main()
