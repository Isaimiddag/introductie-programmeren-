def shout(text: str) -> str:
    """
    >>> shout("hallo")
    "HALLO"
    
    result = ""
    
    for letter in text:
        result += letter.upper()
    return result
        
if __name__ == "__main__":
    text = input("Geef een zin: ")
   
    print(shout(text))
