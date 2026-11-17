def absolute_difference(a : int, b: int) ->:
    difference = abs(a - b)
    return difference

def is_even(n: int) ->bool:
    if n % 2 == 0:
        return True
    else:
        return False
        
def discount(age: int) -> bool:
    if age < 12: 
        return True
    elif age > 65:
        return True
    else:
        return False
    
def sum(n: int) -> int:
    for range(len(n)):
        return n + n

def count_words(words: list[str])
