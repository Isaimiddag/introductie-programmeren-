def get_odd_number() -> int:
    """
    Deze functie vereist een oneven integer.
    """
    result = int(input("Enter an odd int: "))

    while result % 2 == 0:
        result = int(input("Enter an odd int: "))

    return result


def get_positive_int() -> int:
    result = int(input("Geef een positief getal: "))

    while result <= 0:
        result = int(input("Geef een positief getal: "))

    return result


def get_any_int_but_0() -> int:
    result = int(input("Geef een integer verschillend van 0: "))

    while result == 0:
        result = int(input("Geef een integer verschillend van 0: "))

    return result


def get_min_int() -> int:
    result = int(input("Geef een integer van minstens 10: "))

    while result < 10:
        result = int(input("Geef een integer van minstens 10: "))

    return result


def get_two_different_ints() -> tuple[int, int]:
    result1 = int(input("Geef een integer: "))
    result2 = int(input("Geef nog een integer: "))

    while result1 == result2:
        print("FOUT! Voer twee verschillende integers in.")
        result2 = int(input("Geef nog een integer: "))

    return result1, result2


if __name__ == "__main__":
    print(get_odd_number())
    print(get_positive_int())
    print(get_any_int_but_0())
    print(get_min_int())
    print(get_two_different_ints())









