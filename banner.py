greater_than_ten(numbers: list[int]) -> list[int]:
    result = []
    for char in numbers:
        if char > 10:
            numbers.append(char)
        else:
            None
    return result
if __name__ == "__main__":
    lijst = input("Geef een lijst: ")
    
    print(greater_than_ten(lijst))
