def convert(text: str) -> str:
    """
    >>> convert("halloPizza")
    'hallo_pizza'
    >>> convert("readFromFile")
    'read_from_file'
    >>> convert("helloWorld")
    'hello_world'
    >>> convert("camelCase")
    'camel_case'
    >>> convert("myVariableName")
    'my_variable_name'

    >>> convert("aB")
    'a_b'

    >>> convert("python")
    'python'

    >>> convert("FileName")
    'file_name'
    """
    
    result = ""
    for char in text:
        if char.isupper():
            result += "_"+ char.lower()
        else:
            result += char
    return result
    
if __name__ == "__main__":
    camelcase = input("Geef een camelcase: ")
    print(convert(camelcase))