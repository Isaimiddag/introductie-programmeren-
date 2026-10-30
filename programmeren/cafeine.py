def calculate_cafeine(coffee: int, tea: int, energy: int, cola: int) -> int:
    """
    Berekent de hoeveelheid cafeïne op basis van de hoeveelheid gedronken
    drankjes van het type koffie, thee, energiedrank en cola.
    """
    return coffee * 90 + tea * 45 + energy * 80 + cola * 40


if __name__ == "__main__":
    coffee = int(input("Hoeveel koppen koffie? "))
    tea = int(input("Hoeveel koppen thee? "))
    energy = int(input("Hoeveel energiedrankjes? "))
    cola = int(input("Hoeveel glazen cola? "))

    total = calculate_cafeine(coffee, tea, energy, cola)

    print(f"Je krijgt {total} mg cafeïne binnen.")