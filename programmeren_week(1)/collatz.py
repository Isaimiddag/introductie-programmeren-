def print_collatz(n: int) -> None:
    """
    Print de Collatz-reeks van n.

    >>> print_collatz(1)
    1

    >>> print_collatz(3)
    3
    10
    5
    16
    8
    4
    2
    1
    """
    print(n)

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        print(n)


def collatz_length(n: int) -> int:
    """
    Geeft de lengte van de Collatz-reeks van n terug.

    >>> collatz_length(1)
    1

    >>> collatz_length(2)
    2

    >>> collatz_length(3)
    8

    >>> collatz_length(4)
    3

    >>> collatz_length(5)
    6
    """
    length = 1

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        length += 1

    return length