#1
def absolute_difference(a : int, b: int) ->:
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
    for range(len(n)):
        return n + n

#5
def count_words(words: list[str], target: str) -> int:
    count = 0 
    for word in words:
        if word ==
