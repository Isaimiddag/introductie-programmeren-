def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".

    >>> meal("7:00")
    'ontbijt'

    >>> meal("8:00")
    'ontbijt'

    >>> meal("12:15")
    'lunch'

    >>> meal("13:00")
    'lunch'

    >>> meal("18:53")
    'avondeten'

    >>> meal("22:12") is None
    True

    >>> meal("6:59") is None
    True

    >>> meal("17:59") is None
    True
    """
    uur, minuten = time.split(":")
    uur = int(uur)
    minuten = int(minuten)

    tijd = uur * 60 + minuten

    if 420 <= tijd <= 480:
        return "ontbijt"
    elif 720 <= tijd <= 780:
        return "lunch"
    elif 1080 <= tijd <= 1140:
        return "avondeten"
    else:
        return None


if __name__ == "__main__":
    kloktijd = input("Hoe laat is het? ")

    maaltijd = meal(kloktijd)

    if maaltijd is not None:
        print(f"Het is tijd voor {maaltijd}")