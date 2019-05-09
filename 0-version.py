# Relies heavily on
# https://www.bernat.tech/the-state-of-type-hints-in-python/
# https://realpython.com/python-type-checking/#type-systems


# Python 2.7+
def fun1():
    # type: () -> int
    return 42


# Python 3.6+
def fun2() -> int:
    return 42


def fun3():
    """
    :rtype: int
    """
    return 42

