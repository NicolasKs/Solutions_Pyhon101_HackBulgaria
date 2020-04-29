def gen_items(data):
    items = []

    for keys, values in data.items():
        items.append([keys, values])

    return items


def deep_find(data, key):
    items = gen_items(data)

    while items:
        current_item_key = items[0][0]
        current_item_value = items[0][1]
        items.pop(0)

        if current_item_key == key:
            return current_item_value

        if type(current_item_value) == dict:
            items += gen_items(current_item_value)

        if type(current_item_value) == list or type(current_item_value) == tuple:
            for val in current_item_value:
                if type(val) == dict:
                    items += gen_items(val)


def main():
    print(deep_find({'a': 1, 'b': [2, {'f': 8}, 4], 'c': {'d': 5, 'n': 6}}, 'f'))


if __name__ == '__main__':
    main()
