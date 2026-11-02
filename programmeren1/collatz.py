def print_collatz(n: int):
    """
    >>> print(2)
    2
    1
    >>> print(4)
    4
    2
    1
    """
    return len()
    

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

       

if __name__ == "__main__":
   n = int(input("Geef een getal: "))
   print_collatz(n)