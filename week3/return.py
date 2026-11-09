def rotate(lst: list[object]) -> None:
    """
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]

    >>> n2 = ["a", "b", "c", "d"]
    >>> rotate(n2)
    >>> n2
    ['b', 'c', 'd', 'a']

    >>> n3 = [7]
    >>> rotate(n3)
    >>> n3
    [7]

    >>> n4 = [1, 1, 1]
    >>> rotate(n4)
    >>> n4
    [1, 1, 1]

    >>> n5 = [True, False]
    >>> rotate(n5)
    >>> n5
    [False, True]
    """
    first = lst[0]

    for i in range(len(lst) - 1):
        lst[i] = lst[i + 1]

    lst[-1] = first