def is_acidic(ph: float) -> float:
    """
    >>> is_acidic(3.0)
    True
    >>> is_acidic(8.0)
    False
    >>> is_acidic(10)
    False
    >>> is_acidic(2)
    True
    """
    if ph < 7:
        return True
    else:
        return False
    
        
if __name__ == "__main__":
    ph = int(input("Wat is de ph-waarde?: "))
    if is_acidic(ph) == True:
        print("Het is een zuur")
    else:
        print("Het is een base")
    
        
 
            
    