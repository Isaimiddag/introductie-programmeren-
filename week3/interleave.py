def interleave(list1, list2, keep=False):
    """
    Maak een nieuwe lijst met afwisselend elementen uit twee lijsten.

    >>> interleave([1, 2, 3], [4, 5, 6])
    [1, 4, 2, 5, 3, 6]

    >>> interleave(['a', 'b'], ['x', 'y'])
    ['a', 'x', 'b', 'y']

    >>> interleave([1, 2, 3], [4, 5])
    [1, 4, 2, 5]

    >>> interleave([1, 2, 3], [4, 5], True)
    [1, 4, 2, 5, 3]

    >>> interleave([1, 2], [3, 4, 5], True)
    [1, 3, 2, 4, 5]

    >>> interleave([], [1, 2, 3])
    []

    >>> interleave([], [1, 2, 3], True)
    [1, 2, 3]

    >>> interleave([1, 2, 3], [], True)
    [1, 2, 3]

    >>> interleave([], [])
    []
    """
    result = []

    min_len = min(len(list1), len(list2))

    for i in range(min_len):
        result.append(list1[i])
        result.append(list2[i])

    if keep:
        result.extend(list1[min_len:])
        result.extend(list2[min_len:])

    return result
    
    
    