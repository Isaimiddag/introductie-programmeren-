def chunk(lst: list[int], n: int) -> list[list[int]]:
    """
    >>> chunk([1, 2, 3, 4, 5, 6], 2)
    [[1, 2], [3, 4], [5, 6]]
    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    >>> chunk([1, 2, 3], 1)
    [[1], [2], [3]]
    >>> chunk([], 3)
    []
    >>> chunk([1, 2, 3, 4, 5, 6, 7], 3)
    [[1, 2, 3], [4, 5, 6], [7]]

    >>> chunk([5], 2)
    [[5]]
    """
    result = []
    current_chunk = []
    for word in lst:
        current_chunk.append(word)
        if len(current_chunk) == n:
            result.append(current_chunk)
            current_chunk = []
    return result
print(chunk([1, 2, 3], 1))
            
            
            
        




    