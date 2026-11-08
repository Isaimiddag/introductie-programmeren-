def shout(text: str) -> str:
    """
    >>> shout("hallo")
    "HALLO"
    >>> shout("Hello world")
    HELLO WORLD
    >>> shout("Goodmorning everyone")
    "GOODMORNING EVERYONE"
    >>> shout(Who the hell put the muffins the freezer?)
    "WHO THE HELL PUT THE MUFFINS THE FREEZER?"
    """
    result = ""
    for letter in text:
        result += letter.upper()
    return result
        
if __name__ == "__main__":
    text = input("Geef een zin: ")
   
    print(shout(text))
