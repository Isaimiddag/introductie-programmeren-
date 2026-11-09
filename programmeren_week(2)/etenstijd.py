def meal(time: str) -> str:
    """
    >>> meal("7:00")
    "ontbijt"
    >>> meal("8:00")
    ontbijt"
    >>> meal("12:15")
    lunch
    >>> meal("13:00")
    lunch
    >>> meal("18:53")
    avondeten
    """
    uur, minuten = time.split(":")
    uur = int(uur)
    minuten = int(minuten)
    tijd = uur * 60 + minuten
    
    if tijd >= 420 and tijd <= 480:
        return "ontbijt"
    elif tijd >= 720 and tijd <= 780:
        return "lunch"
    elif tijd >= 1080 and tijd <= 1140:
        return "avondeten"
    else:
        return None

if __name__ == "__main__":
    kloktijd = input("Hoe laat is het? ")
    maaltijd = meal(kloktijd)
    if maaltijd is not None:
        print(f"{maaltijd}")
    