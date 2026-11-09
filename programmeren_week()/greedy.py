def count_coins(cents: int) -> int:
    """
    Berekent het minimale aantal munten (25, 10, 5 en 1 cent)
    waarmee het bedrag `cents` kan worden teruggegeven.

    >>> count_coins(0)
    0

    >>> count_coins(1)
    1

    >>> count_coins(10)
    1

    >>> count_coins(22)
    4

    >>> count_coins(41)
    4

    >>> count_coins(78)
    6

    >>> count_coins(108)
    8
    """
    coins = 0

    while cents >= 25:
        cents -= 25
        coins += 1

    while cents >= 10:
        cents -= 10
        coins += 1

    while cents >= 5:
        cents -= 5
        coins += 1

    while cents >= 1:
        cents -= 1
        coins += 1

    return coins


if __name__ == "__main__":
    amount = float(input("Hoeveel wisselgeld moet er gegeven worden? "))

    while amount < 0:
        amount = float(input("Hoeveel wisselgeld moet er gegeven worden? "))

    cents = round(amount * 100)

    print(count_coins(cents))