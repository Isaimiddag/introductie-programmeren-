def print_pyramid(hoogte: int) -> None:
    """
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
        print("#" * (rij + 1))