def print_pyramid(hoogte: int) -> None:
    """
    Print een halve piramide.

    >>> print_pyramid(3)
    ##
    ###
    ####

    >>> print_pyramid(1)
    ##
    """
    while hoogte
    for rij in range(1, hoogte + 1):
        print("#" * (rij + 1))


if __name__ == "__main__":
    hoogte = int(input("Hoe hoog moet de piramide zijn? "))
    print_pyramid(hoogte)