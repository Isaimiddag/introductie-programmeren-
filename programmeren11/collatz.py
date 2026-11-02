def print_collatz(n: int) -> None:
    """
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