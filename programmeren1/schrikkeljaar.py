def is_schrikkel(year: int) -> bool:
    """
    >>> is_schrikkel(2024)
    True
    >>> is_schrikkel(2025)
    False
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(1900)
    False
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    year = int(input("Geef een jaartal: "))

    if is_schrikkel(year):
        print(f"{year} is een schrikkeljaar")
    else:
        print(f"{year} is geen schrikkeljaar")