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
    kleinste_nummer = l[0]
    for i in range(len(l)):
        if l[i] is < kleinste_nummer:
            kleinste_nummer = l[i]
            l[i]
        
    
    return new_list
    
if __name__ == "__main__":
    p = input("geef een lijst: ")
    print(selection_sort(p))
    