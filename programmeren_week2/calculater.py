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
    
    if y == "*":
        return float(x*z)
    elif y == "/":
        return float(x/z)
    elif y == "-":
        return float(x-z)
    elif y == "+":
        return float(x+z)
    else:
        return None
    

if __name__ == '__main__':
    som = input()
    x, y, z = som.split()
    x = int(x)
    z = int(z)
    antwoord = evaluate(x, y, z)
    print(antwoord)