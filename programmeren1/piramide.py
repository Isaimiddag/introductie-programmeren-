def print_pyramid(hoogte: int) -> None:
    """
    Print een halve piramide.

    >>> print_pyramid(1)
    ##

    >>> print_pyramid(3)
      ##
     ###
    ####

    >>> print_pyramid(5)
        ##
       ###
      ####
     #####
    ######
    """
    for rij in range(1, hoogte + 1):

        # Spaties
        for _ in range(hoogte - rij):
            print(" ", end="")

        # Hekjes
        for _ in range(rij + 1):
            print("#", end="")

        # Nieuwe regel
        print()


if __name__ == "__main__":
    hoogte = int(input("Hoe hoog moet de piramide zijn? "))

    while hoogte < 1 or hoogte > 23:
        hoogte = int(input("Hoe hoog moet de piramide zijn? "))

    print_pyramid(hoogte)