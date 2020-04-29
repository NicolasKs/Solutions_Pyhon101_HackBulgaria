import random
from string import ascii_letters


def generate_word():
    while True:
        length = random.randint(1, 10)
        word = ''.join(random.sample(ascii_letters, length))
        yield word


def generate_filename():
    file_number = 0
    while True:
        file_number += 1
        yield f'{file_number}.txt'


def generate_chapter(chapter_length):
    word = generate_word()
    chapter_num = 1

    while True:
        chapter = ''
        chapter += f'# Chapter {chapter_num}\n'
        chapter_num += 1
        for i in range(chapter_length):
            chapter += next(word)
            chapter += ' '
        chapter += f'\n\n'
        yield chapter


def generate_files(chapter_length, total_chapters):
    file_name = generate_filename()
    chapter = generate_chapter(chapter_length)
    chapters_per_file = 5

    while total_chapters > 0:

        if (total_chapters - chapters_per_file) < 0:
            chapters_per_file = total_chapters

        with open(next(file_name), 'w') as f:
            for i in range(chapters_per_file):
                f.write(next(chapter))

        total_chapters -= chapters_per_file


def user_input():
    chapter_length = int(input('Enter chapter length: '))
    total_chapters = int(input('Enter a number of chapters: '))
    generate_files(chapter_length, total_chapters)


def main():
    user_input()


if __name__ == '__main__':
    main()
