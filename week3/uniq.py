def uniq(lst: list[object]) -> list[object]:
    """
    
    """
    result = []
    for item in lst:
        if item in lst:
            item.remove()
    