import functools


def noop(f):
    def noop_wrapper():
        return f()
    return noop_wrapper


@noop
def hello():
    """ Prints a well-know message """
    print('hello_obj world!')


# print(help(hello))
print(hello.__name__)
print(hello.__doc__)
