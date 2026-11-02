def travel_costs(km: int) -> float:
    """
    Bepaalt de vervoerskosten op basis van de te rijden afstand
    naar de accommodatie (heen en terug).

    >>> travel_costs(100)
    26.0

    >>> travel_costs(200)
    52.0

    >>> travel_costs(0)
    0.0
    """
    return km * 0.13 * 2


def overnight_costs(nights: int) -> float:
    """
    Bepaalt de overnachtingskosten op basis van het aantal nachten.

    >>> overnight_costs(3)
    180.0

    >>> overnight_costs(5)
    300.0

    >>> overnight_costs(0)
    0.0
    """
    return nights * 60.0


def total_costs(km: int, nights: int) -> int:
    """
    Bepaalt de totale kosten op basis van de afstand en het aantal
    nachten en rondt af naar hele euro's.

    >>> total_costs(1250, 5)
    625

    >>> total_costs(800, 10)
    808

    >>> total_costs(2159, 12)
    1281
    """
    total = travel_costs(km) + overnight_costs(nights)
    return int(total + 0.5)


if __name__ == "__main__":
    km = int(input("Hoe ver ga je weg in kilometers? "))
    nights = int(input("Hoe veel nachten is je verblijf? "))

    total = total_costs(km, nights)

    print(f"Jouw vakantie kost: {total}")