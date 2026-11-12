def chunk(lst: list[int], lst2: list[int]) -> list:
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

    for i in range(0, len(lst), n):
        result.append(lst[i:i+n])

    return result


if __name__ == "__main__":
    rij = input("Geef getallen gescheiden door spaties: ").split()

    for i in range(len(rij)):
        rij[i] = int(rij[i])

    n = int(input("Grootte van de stukken: "))

    print(chunk(rij, n))
    