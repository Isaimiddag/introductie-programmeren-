def evaluate(x: int, y: str, z: int) -> float:
    """
    >>> evaluate( 2, "*", 2)
    4.0
    >>> evaluate(10, "+", 2)
    12.0
    >>> evaluate(2, "/", 2)
    1.0
    >>> evaluate(2, "*", 3)
    6.0
    >>> evaluate(8, "-", 4)
    4.0
    """
    formule = evaluate.split(x,y,z)
    x = int(x)
    y = str(y)
    z = int(z)
    
    if y == "*":
        return x*z
    elif y == "/":
        return x/z
    elif y == "-":
        return x-z
    elif y == "+":
        return x+z
    else:
        return None
    

if __name__ == '__main__':
    som = input("Geef een som: ")
    antwoord = evaluate(som)
    if antwoord is not None:
        print(antwoord)