def compress(iterable, mask):
    for val in range(len(iterable)):
        if mask[val]:
            yield iterable[val]


def main():
    iterable = ["Ivo", "Rado", "Panda"]
    mask = [False, False, True]
    res = list(compress(iterable, mask))
    print(res)


if __name__ == '__main__':
    main()
