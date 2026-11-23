def merge_lists(lst1, lst2):
    """
    Voegt twee gesorteerde lijsten samen tot één gesorteerde lijst.

    >>> merge_lists([1, 2, 5], [4, 5, 6])
    [1, 2, 4, 5, 5, 6]

    >>> merge_lists([1, 3, 7], [2, 4, 6])
    [1, 2, 3, 4, 6, 7]

    >>> merge_lists([], [1, 2, 3])
    [1, 2, 3]

    >>> merge_lists([1, 2, 3], [])
    [1, 2, 3]
    """
    result = []

    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1

    
    for k in range(i, len(lst1)):
        result.append(lst1[k])

    # Voeg resterende elementen van lst2 toe
    for k in range(j, len(lst2)):
        result.append(lst2[k])

    return result