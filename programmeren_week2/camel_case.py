def convert(text: str) -> str:
    """
    >>> convert("halloPizza)
    "hallo_pizza"
    >>> convert(readFromFile)
    "read_from_file"
    >>> convert("helloWorld")
    "hello_world"
    >>> convert("camelCase")
    "camel_case"
    """
    
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
            
            