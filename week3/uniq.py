def uniq(lst: list[object]) -> list[object]:
    """
    >>> uniq([1, 2, 3])
    [1, 2, 3]
    >>> uniq([1, 1, 2, 2, 3])
    [1, 2, 3]
    >>> uniq([3, 1, 3, 2, 1])
    [3, 1, 2]
    >>> uniq([])
    []
    >>> uniq(["a", "a", "b", "a"])
    ['a', 'b']
    """
    result = []
    for item in range(len(lst)):
        if item not in result:
            result.append(lst[item])
    return result
    
if __name__ == "__main__":
    pep= input("Wat is uw rij? ")
    print(uniq(pep))
    