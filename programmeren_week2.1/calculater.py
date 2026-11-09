def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.

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

    >>> evaluate(100, "-", 9)
    91.0

    >>> evaluate(3, "/", 8)
    0.375

    >>> evaluate(-5, "+", 2)
    -3.0

    >>> evaluate(-10, "-", -5)
    -5.0
    """
    if y == "*":
        return float(x * z)
    elif y == "/":
        return float(x / z)
    elif y == "-":
        return float(x - z)
    elif y == "+":
        return float(x + z)


if __name__ == "__main__":
    som = input("Geef een som: ")

    x, y, z = som.split()

    x = int(x)
    z = int(z)

    antwoord = evaluate(x, y, z)

    print(antwoord)
