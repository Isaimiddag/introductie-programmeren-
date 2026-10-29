def is_acidic(ph: float):
    """
    >>> is_acidic(3.0)
    True
    
    >>> is_acidic(8.0)
    False
    """
if __name__ == "__main__":
    ph = int(input("Wat is de ph-waarde?: "))
    if ph < 7:
        print("Het is een zuur.")
    else:
        print("Het is geen zuur.")
        
            
    