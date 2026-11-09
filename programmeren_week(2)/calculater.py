def evaluate(x: int, y: str, z: int) -> float:
 >>> evaluate(2, "*", 2)
    4.0
    >>> evaluate(10, "+", 2)
    12.0
    >>> evaluate(2, "/", 2)
    1.0
    >>> evaluate(2, "*", 3)
    6.0
    >>> evaluate(8, "-", 4)
    4.0
    >>> evaluate(4, "*", -6)
    -24.0

    >>> evaluate(7, "+", 3)
    10.0
    >>> evaluate(15, "-", 20)
    -5.0
    >>> evaluate(-3, "*", 4)
    -12.0
    >>> evaluate(-8, "/", 2)
    -4.0
    >>> evaluate(-5, "+", -5)
    -10.0
    """
    
    if y == "*":
        return float(x*z)
    elif y == "/":
        return float(x/z)
    elif y == "-":
        return float(x-z)
    elif y == "+":
        return float(x+z)

    

if __name__ == '__main__':
    som = input("geef een som: ")
    x, y, z = som.split()
    x = int(x)
    z = int(z)
    antwoord = evaluate(x, y, z)
    print(antwoord)