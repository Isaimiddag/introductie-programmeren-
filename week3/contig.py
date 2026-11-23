def contig(lst: lst[int) -> list[int]:
    """
    >>> contig([1, 2, 3, 5, 6, 9])
    [[1, 2, 3], [5, 6], [9]]
    >>> contig([1, 3, 5])
    [[1], [3], [5]]
    >>> contig([1, 2, 4, 5, 6, 10])
    [[1, 2], [4, 5, 6], [10]]
    >>> contig([])
    []
    >>> contig([7])
    [[7]]
    """
    if len(lst) == 0:
        return []

    result = []
    groep = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            groep.append(lst[i])
        else:
            result.append(groep)
            groep = [lst[i]]

    result.append(groep)
    return result