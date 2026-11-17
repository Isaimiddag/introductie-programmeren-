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
    
