def cycle(iterable):
    while True:
        for val in iterable:
            yield val


def main():
    endless = cycle(range(0, 10))
    for val in endless:
        print(val)


if __name__ == '__main__':
    main()
