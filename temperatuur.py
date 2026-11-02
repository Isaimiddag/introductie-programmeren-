def convert_temperature(old_type: str, old_temp: int) -> int:
    """
    Zet de temperatuur (old_temp) van het type old_type om naar
    de temperatuur van het nieuwe type.

    >>> convert_temperature("C", 0)
    32
    >>> convert_temperature("C", 20)
    68
    >>> convert_temperature("F", 32)
    0
    >>> convert_temperature("F", 0)
    -17
    >>> convert_temperature("c", 10)
    50
    """
    if old_type.upper() == "C":
        return int((18 * old_temp + 320) / 10)
    else:
        return int((10 * old_temp - 320) / 18)


def print_table(old_type: str,
                begin_temp: int,
                end_temp: int,
                step_size: int) -> None:
    """
    Print de conversie-tabel.

    >>> print_table("C", 0, 10, 5)
      C |   F
      0 |  32
      5 |  41
     10 |  50

    >>> print_table("F", 0, 4, 2)
      F |   C
      0 | -17
      2 | -16
      4 | -15
    """
    old_type = old_type.upper()

    if old_type == "C":
        new_type = "F"
    else:
        new_type = "C"

    print(f"{old_type:>3} | {new_type:>3}")

    for temp in range(begin_temp, end_temp + 1, step_size):
        new_temp = convert_temperature(old_type, temp)
        print(f"{temp:>3} | {new_temp:>3}")


if __name__ == "__main__":
    old_type = input("Welke eenheid van temperatuur (C of F)? ")

    while old_type.upper() not in ["C", "F"]:
        old_type = input("Welke eenheid van temperatuur (C of F)? ")

    begin_temp = int(input("Wat is de begintemperatuur? "))
    end_temp = int(input("Wat is de eindtemperatuur? "))

    step_size = int(input("Wat is de stapgrootte? "))

    while step_size <= 0:
        step_size = int(input("Wat is de stapgrootte? "))

    print_table(old_type, begin_temp, end_temp, step_size)