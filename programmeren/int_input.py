def get_odd_number() -> int:
    """
    Deze functie vereist een oneven integer.
    """
    result = int(input("Enter an odd int: "))
    while result % 2 == 0:
        result = int(input("Enter an odd int: "))
    return result


def get_positive_int():
    result = int(input("geef een integer: "))
    if result > 0:
        print(f"{result} is an integer")
    else:
        print("Dit is geen integer.")
        
def get_any_int_but_0():
    result = int(input("geef een integer: "))
    if result != 0:
        print(f"{result} is an integer")
    elif result == 0:
        print("Dit is een 0, voer iets anders in.")   
    
def get_min_int():
    result = int(input("geef een integer: "))
    if result < 10:
        print(f"geef een integer hoger dan{result}")
    else:
        print("Wat een mooie integer")

def get_two_different_ints():
    result1 = int(input("geef een integer: "))
    result2 = int(input("geef nog een integer: "))
    if result1 == result2:
        print("FOUT! Je hebt twee dezelfde integers ingevoerd. Voer 2 verschillende in")
    else:
        print("GOED! Je hebt twee verschillende integers ingevoerd!")











