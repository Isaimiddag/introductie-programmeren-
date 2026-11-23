def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    >>> l([1,2,5,3])
    [1,2,3,4,5]
    >>> ([2,1,3])
    [1,2,3]
    >>> ([3,4,1,2])
    [1,2,3,4]
    >>> ([1,2])
    [1,2]
    """
    for nummer in l:
        if 