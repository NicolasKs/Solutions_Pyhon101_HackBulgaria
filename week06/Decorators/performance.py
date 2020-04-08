import time
from datetime import datetime


def performance(filename):

    def decorator(func):

        def wraper():
            start_time = datetime.now()
            func()
            end_time = (datetime.now() - start_time).total_seconds()
            with open(filename, 'a') as f:
                f.write(f'{func.__name__} was called and took {round(end_time,2)} secounds to complete\n')

        return wraper

    return decorator


@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return print('I am done!')


def main():
    something_heavy()


if __name__ == '__main__':
    main()
