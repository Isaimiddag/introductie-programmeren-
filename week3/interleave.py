def interleave(lst1: list, lst2: list) -> list:
    lijst = []
    for item in lst1:
        if item.odd:
            lijst.append(item)
    for item in lst2:
        if item.even:
            lijst.append(item)
    return lijst
if __name__ == "__main__":
    