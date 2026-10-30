def hoeveelheid_water(minuten: int) -> int:
    
    """
    >>> hoeveelheid_water(10)
    120
    
    >>> hoeveelheid_water(5)
    60
    
    >>> hoeveelheid_water(1)
    12
    """
    return minuten * 12
    

if __name__ == "__main__":
    minuten = int(input("hoeveelheid minuten douchen: "))
    print(minuten)
    