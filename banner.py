def greater_than_ten(numbers: list[int]) -> list[int]:
    result = []
    for char in numbers:
        if char > 10:
            result.append(char)

    return result
    
if __name__ == "__main__":
    lijst = [int(x) for x in input("Geef een lijst: ").split()]
    print(greater_than_ten(lijst))
    

def count_vowel(s: str) -> int:
    