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
    for i in range(len(lst)):
        if item not in result:
            result.append(lst[item])
    return result
    
if __name__ == "__main__":
    rij = input("Wat is uw rij? ").split()
    print(uniq(rij))