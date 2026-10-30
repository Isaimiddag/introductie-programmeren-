def get_odd_number() -> int:
    """
    Deze functie vereist een oneven integer.
    """
    result = int(input("Enter an odd int: "))
    while result % 2 == 0:
        result = int(input("Enter an odd int: "))
    return result
    
get_positive_int = int(input("Geef een integer: "))
if get_positive_int != int:
    print("Dat is geen integer, voer een integer in!")

get_odd_number(get_positive_int)
