def print_collatz(n: int) -> int:
    """
    >>> print(2)
    2
    1
    >>> print(4)
    4
    2
    1
    """
    count = 0
    
    
def collatz_length()
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            count += 1
        else:
            n = 3 * n + 1
            count += 1
    return count

       

if __name__ == "__main__":
    n = int(input("Geef een getal: "))
    hallo = print_collatz(n)
    print(hallo)