def interleave(lst1: list, lst2: list) -> list:
    lijst = []
    for item in lst1:
        if item.odd:
            lst1.append(item)
        