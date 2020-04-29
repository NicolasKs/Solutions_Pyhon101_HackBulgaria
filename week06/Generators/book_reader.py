from zipfile import ZipFile
from get_char import Getch


def get_chapters(filename):
    with ZipFile(filename, 'r') as z:
        for file in z.namelist():
            with z.open(file, 'r') as f:
                for line in f.readlines():
                    line = line.decode("utf-8")
                    if line[0] == '#':
                        print(line)
                        yield
                    else:
                        print(line)


def check_input():
    get_input = Getch()
    user_input = get_input()

    if user_input == ' ':
        return True

    print('Press Space to continue')
    return check_input()


def read_chapters(generator):
    for chapter in generator:
        check_input()


def main():
    chapters = get_chapters('Book.zip')

    read_chapters(chapters)


if __name__ == '__main__':
    main()
