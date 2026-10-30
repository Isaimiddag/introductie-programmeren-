def travel_costs(km: int) -> float:
    """
    >>> travel_costs(100)
    13
    
    >>> travel_costs(50)
    
    return km * 0.13
    
    




if __name__ == "__main__":
    kosten_per_km = 0.13
    kosten_per_nacht = 60
    
    reiskilometers = int(input(f"Hoeveel km reist u naar uw bestemming?: "))
    reiskosten = reiskilometers * kosten_per_km *2
    print(f"Dan kost u heen en terug reis {reiskosten} euro")
    
    kosten_overnachten = int(input(f"Hoeveel nachten blijft u overnachten?: "))
    totale_kosten_overnachten = kosten_overnachten * 60
    print(f"Uw overnachtingen kosten {totale_kosten_overnachten} euro.")
    
    totale_kosten = int(totale_kosten_overnachten + reiskosten)
    
    print(f"De totale kosten van uw reis en overnachtingen {totale_kosten} euro")
    
    