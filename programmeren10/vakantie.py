def travel_costs(km: int) -> float:
    """
    >>> travel_costs(100)
    26.0
    
    >>> travel_costs(200)
    52.0
    """
    return km * 0.13 * 2

def overnight_costs(nights: int) -> float:
    """
    >>> overnight_costs(3)
    180.0
    
    >>> overnight_costs(5)
    300.0
    """
    return nights * 60
    
def total_costs(km: int, nights: int) -> float:
    """
    >>> total_costs(100, 5)
    326.0
    >>> total_costs(10,2)
    122.6
    """
    return km*0.13 *2 + nights*60

if __name__ == "__main__":
    km = int(input("Hoeveel kilometer reis je naar je bestemming? "))
    nights = int(input("Hoeveel nachten overnacht je? "))
    totale_prijs = total_costs(km, nights)
    print(f"totale prijs is {totale_prijs}")
    
    
    
    
    
  