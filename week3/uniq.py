def uniq(lst: list[object]) -> list[object]:
    """
    
    """
    result = []
    for item in range(len(lst)):
        if item in lst:
            lst(item.remove())
    