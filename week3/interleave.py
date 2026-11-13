def interleave(lst1: list, lst2: list, keep: bool) -> list:
    """
    Maak een nieuwe lijst met afwisselend elementen uit lst1 en lst2.

    >>> interleave([1, 2, 3], [4, 5, 6], False)
    [1, 4, 2, 5, 3, 6]

    >>> interleave([1, 2], [3, 4, 5], False)
    [1, 3, 2, 4]

    >>> interleave([1, 2], [3, 4, 5], True)
    [1, 3, 2, 4, 5]

    >>> interleave([1, 2, 3, 4], [5], True)
    [1, 5, 2, 3, 4]

    >>> interleave([], [1, 2], True)
    [1, 2]

    >>> interleave([], [1, 2], False)
    []
    """
    resultaat = []

    kortste = min(len(lst1), len(lst2))

    for i in range(kortste):
        resultaat.append(lst1[i])
        resultaat.append(lst2[i])

    if keep:
        resultaat.extend(lst1[kortste:])
        resultaat.extend(lst2[kortste:])

    return resultaat 

