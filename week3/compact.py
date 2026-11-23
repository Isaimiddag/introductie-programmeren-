def compact(lst: list[object]) -> list[object]:
    """
    >>> compact([1, 2, 3])
    [1, 2, 3]

    >>> compact([0, 1, 0, 2])
    [1, 2]

    >>> compact(["", "hallo", "", "wereld"])
    ['hallo', 'wereld']

    >>> compact([False, True, False])
    [True]

    >>> compact([0, "", None, [], "python", 5])
    ['python', 5]
    """
    result = []
    for char in lst: 
        if x:
            result.append(char)
    return result
print(compact([0, 1, 0, 2])
)