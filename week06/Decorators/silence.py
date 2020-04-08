def silence(filename):

    def decorator(func):

        def wraper(*args):

            try:
                func(*args)
            except Exception as exc:
                with open(filename, 'a') as f:
                    f.write(f'Calling {func.__name__} raised an error - {exc.__class__.__name__}:'
                            f' "{str(exc)}" . Provided arguments: {args}\n')

        return wraper

    return decorator


@silence('errors.txt')
def foo(x):
    if x > 50:
        raise ValueError('Omg.')


def main():
    foo(10)
    foo(100)


if __name__ == '__main__':
    main()
