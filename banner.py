# vraag 1
def greater_than_ten(numbers: list[int]) -> list[int]:
    result = []
    for char in numbers:
        if char > 10:
            result.append(char)

    return result
    
if __name__ == "__main__":
    lijst = [int(x) for x in input("Geef een lijst: ").split()]
    print(greater_than_ten(lijst))
    
# vraag 2
def count_vowel(s: str) -> int:
    count = 0
    for char in s:
        if begin_woord == True:
            if char in "aeiouAEIOU":
                count += 1
            begin_woord = False
        if char == " ":
            begin_woord = True

    return count
if __name__ == "__main__":
    string = input("Geef wat woorden: ")
    aantal = count_vowel(string)
    print(aantal)
    
# vraag 3   
def reverse_string(s: str) -> str:
    new_s = " "
    for char in s:
        for i in range(len(s)):

# vraag 4
def double_letters(words: list[str]) -> list[str]:
    double_letter_words = []
    for char in words:
        for
            
            