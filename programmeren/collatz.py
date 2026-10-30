def print_collatz(n):
    print(n)

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        print(n)

if 
n = int(input("Geef een getal: "))
print_collatz(n)