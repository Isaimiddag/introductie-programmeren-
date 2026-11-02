hoogte = int(input("Hoe hoog moet de piramide zijn? "))
"""
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

while hoogte < 1 or hoogte > 23:
    hoogte = int(input("Hoe hoog moet de piramide zijn? "))

for rij in range(1, hoogte + 1):

    for _ in range(hoogte - rij):
        print(" ", end="")

    for _ in range(rij + 1):
        print("#", end="")

    print()