def calculate_years(start_size: int, end_size: int) -> int:
    """
    Berekent het aantal jaar dat het duurt voor de populatie om
    end_size te bereiken.

    >>> calculate_years(1200, 1300)
    1
    >>> calculate_years(1000, 2000)
    8
    >>> calculate_years(1250, 1300)
    1
    >>> calculate_years(1270, 1300)
    1
    >>> calculate_years(1280, 1300)
    1
    >>> calculate_years(1290, 1300)
    1
    """
    years = 0
    population = start_size

    while population < end_size:
        population = population + population // 3 - population // 4
        years += 1

    return years


if __name__ == '__main__':
    start_size = int(input("Start population: "))
    while start_size < 9:
        start_size = int(input("Start population: "))

    end_size = int(input("End population: "))
    while end_size < start_size:
        end_size = int(input("End population: "))

    result = calculate_years(start_size, end_size)
    

    print(f"Years: {result}")