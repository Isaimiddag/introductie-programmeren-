#1
def absolute_difference(a : int, b: int) -> int:
    difference = abs(a - b)
    return difference
#2
def is_even(n: int) ->bool:
    if n % 2 == 0:
        return True
    else:
        return False
 #3      
def discount(age: int) -> bool:
    if age < 12: 
        return True
    elif age > 65:
        return True
    else:
        return False
#4   
def sum(n: int) -> int:
    #for len(n):
        return n + n

#5
def count_words(words: list[str], target: str) -> int:
    count = 0 
    for word in words:
        if word == target:
            count += 1
    return count
#6
def maximum(numbers: list[int]) -> int:
    huidige_max = 0
    for number in numbers:
        if number > huidige_max:
            huidige_max == number
    return huidige_max
    
#7
def even_numbers(numbers: list[int]) -> list[int]:
    even_numbers = []
    for number in numbers: 
        if number % 2 == 0:
            number += even_numbers
    return even_numbers
#8
def meal(time: str) -> str:
    uur, min = time.split(:)
     = 60
