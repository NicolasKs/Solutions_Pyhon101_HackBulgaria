from zipfile import ZipFile


def read_zip(filename):
    with ZipFile(filename, 'r') as z:
        for file in z.namelist():
            with z.open(file, 'r') as f:
                read_files(f)


def read_files(file):
    for line in file.readlines():
        line = line.decode("utf-8")
        check_chapter(line)


def check_chapter(line):
    if line[0] == '#':
        print(line)
        yield
    else:
        print(line)


def main():
    a = read_zip('Book.zip')

    for i in a:
        print('kaval')


if __name__ == '__main__':
    main()
