# vraag 1
def greater_than_ten(numbers: list[int]) -> list[int]:
    result = []
    for char in numbers:
        if char > 10:
            result.append(char)

    return result
    

# vraag 2
def count_vowel(s: str) -> int:
    count = 0
    begin_woord = True
    for char in s:
        if begin_woord == True:
            if char in "aeiouAEIOU":
                count += 1
            begin_woord = False
        if char == " ":
            begin_woord = True
    return count


# vraag 3   
def reverse_string(s: str) -> str:
    new_s = ""
    for char in s:
        new_s = char + new_s
    return new_s

# vraag 4
def double_letters(words: list[str]) -> list[str]:
    result = []
    for word in words:
        for x in range(len(words)):
            if word[x] == word[x+1]:
                result.append(word)
    return result

#vraag 5
#Formule:(aantal klinkers)×(gemiddelde woordlengte)
def text_score(s: str) -> float:
    aantal_klinkers = 0
    aantal_spaties = 0
    aantal_letters = 0
    for char in s:
        if char.isalpha:
            aantal_letters += 1
        if char in "aeiouAEIOU":
            aantal_klinkers += 1
        elif char == " ":
            aantal_spaties += 1
    aantal_woorden = aantal_spaties + 1
    gemiddelde_lengte = aantal_letters / aantal_woorden
    score = aantal_klinkers * gemiddelde_lengte 
        retun round(score, 2)
        
    
            
            
            