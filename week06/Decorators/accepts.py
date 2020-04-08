def accepts(*args):
    check_types = [typ for typ in args]

    def function_wrapper(func):

        def function_args_checker(*args):
            for ind, value in enumerate(args):
                if type(value) != check_types[ind]:
                    raise TypeError(f'Argument {func.__code__.co_varnames[ind]}'
                                    f' of {func.__name__} is not {check_types[ind]}')
            return func(*args)

        return function_args_checker

    return function_wrapper


@accepts(str)
def say_hello(name):
    print("Hello, I am {}".format(name))


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))


def main():
    deposit("Marto", 10)
    # say_hello(4)


if __name__ == '__main__':
    main()
