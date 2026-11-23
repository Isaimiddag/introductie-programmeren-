def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.

    >>> selection_sort([1, 2, 3])
    >>> selection_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> selection_sort([1, 2, 3])
    [1, 2, 3]
    >>> selection_sort([7])
    [7]
    >>> selection_sort([])
    []
    >>> selection_sort([4, 2, 4, 1])
    [1, 2, 4, 4]
    """
    for i in range(len(l)):
        min_index = i

        for j in range(i + 1, len(l)):
            if l[j] < lmin_index = j

        l[i], l[min_index] = l[min_index], l[i]

    return l
    