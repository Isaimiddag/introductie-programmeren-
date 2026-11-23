def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    >>> l([1,2,5,3])
    [1,2,3,4,5]
    >>> l([2,1,3])
    [1,2,3]
    >>> l([3,4,1,2])
    [1,2,3,4]
    >>> l([1,2])
    [1,2]
    """
    new_list = l.sort()
    return new_list
if __name__ == "__main__":
    p = input("geef een lijst: ")
    print(selection_sort(p))
    