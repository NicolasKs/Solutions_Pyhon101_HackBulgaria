def chain(iterable_one, iterable_two):
    for value in iterable_one:
        yield value
    for value in iterable_two:
        yield value


def main():
    res = list(chain(range(1, 4), range(4, 7)))
    print(res)


if __name__ == '__main__':
    main()
