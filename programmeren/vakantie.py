if __name__ = "__main__":
    kosten_per_km = 0.13
    kosten_per_nacht = 60
    
    reiskilometers = int(input(f"Hoeveel km reist u naar uw bestemming?: "))
    reiskosten = reiskilometers * kosten_per_km *2
    print(f"Dan kost u heen en terug reis {reiskosten} euro")
    
    
    
    