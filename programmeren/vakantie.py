def travel_costs(km: int) -> float:
    """
    >>> travel_costs(100)
    26
    
    >>> travel_costs(200)
    52
    """
    return km * 0.13 * 2

def overnight_costs(nights: int) -> float:
    """
    >>> overnight_costs(3)
    180
    
    >>> overnight_costs(5)
    300
    """
    return nights * 60
    
def total_costs(km: int, nights: int) -> int:
    """
    >>> total_costs(100, 5)
    326
    """
    return km*0.13 *2 + nights*60

if __name__ == "__main__":
    km = int(input("Hoeveel kilometer reis je naar je bestemming? "))
    nights = int(input("Hoeveel nachten overnacht je? "))
    totale_prijs = total_costs(km: int, nights
    
    
    
    
    
  