def deep_find(data, key):
    for curr_key in data:
        res = deeper(data[curr_key], curr_key, key)
        if res is not None:
            return res


def deeper(data, curr_key, key):
    if curr_key == key:
        return data

    if type(data) == dict:
        return deep_find(data, key)

    if type(data) == list or type(data) == tuple:
        new = {}
        for val in data:
            if type(val) == dict:
                new.update(val)
        return deep_find(new, key)


def main():
    print(deep_find({'k': {'m': {'g': 4}, 'h': {'s': 1}}, 'f': 7, 'a': {'b': {'c': {'d': 5}}}}, 'd'))
    print(deep_find({'a': [1, 2, {'c': 6}, {'b': 5}]}, 'b'))


if __name__ == '__main__':
    main()
