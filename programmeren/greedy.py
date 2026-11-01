def count_coins(cents: int) -> int:
    """
    Berekent het minimale aantal munten (25, 10, 5 en 1 cent)
    waarmee het bedrag `cents` kan worden teruggegeven.
    
    >>> count_coins(10)
    1
    >>> count_coins(22)
    4
    >>> count_coins(78)
    6
    
    """


    coins = 0

    coins += cents // 25
    cents = cents % 25

    coins += cents // 10
    cents = cents % 10

    coins += cents // 5
    cents = cents % 5

    coins += cents

    return coins


if __name__ == '__main__':
    cents = int(input("Hoeveel cent wisselgeld? "))
    print(count_coins(cents))