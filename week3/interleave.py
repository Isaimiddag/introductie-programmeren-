def interleave(lst1: list[int], lst2: list[int], keep: bool) -> list[int]:
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
    
    
    