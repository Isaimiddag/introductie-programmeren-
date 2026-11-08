def convert(text: str) -> str:
    """
    >>> convert("halloPizza)
    
    
    result = ""
    for char in text:
        if char.isupper():
            result += "_"+ char.lower()
        else:
            result += char
    return result
    
if __name__ == "__main__":
    input = input("Geef een camelcase: ")
    print(convert(input))
            
            