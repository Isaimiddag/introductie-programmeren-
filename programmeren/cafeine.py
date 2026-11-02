def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    Berekent de hoeveelheid cafeÔne op basis van de hoeveelheid gedronken
    drankjes van het type koffie, thee, energiedrank en cola.

    >>> calculate_cafeine(1, 0, 0, 0)
    90

    >>> calculate_cafeine(0, 1, 0, 0)
    45

    >>> calculate_cafeine(0, 0, 1, 0)
    80

    >>> calculate_cafeine(0, 0, 0, 1)
    40

    >>> calculate_cafeine(1, 1, 1, 1)
    255

    >>> calculate_cafeine(2, 3, 1, 4)
    475

    >>> calculate_cafeine(0, 0, 0, 0)
    0

    >>> calculate_cafeine(5, 0, 0, 0)
    450
    """
    return coffee * 90 + tea * 45 + energy * 80 + cola * 40


if __name__ == "__main__":
    coffee = int(input("Hoeveel koppen koffie? "))
    tea = int(input("Hoeveel koppen thee? "))
    energy = int(input("Hoeveel energiedrankjes? "))
    cola = int(input("Hoeveel glazen cola? "))

    total = calculate_cafeine(coffee, tea, energy, cola)

    print(f"Je krijgt {total} mg cafe√Øne binnen.")