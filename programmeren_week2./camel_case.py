def convert(text: str) -> str:
    """
    >>> convert("check")
    'check'

    >>> convert("convertInput")
    'convert_input'

    >>> convert("readFromFile")
    'read_from_file'

    >>> convert("helloWorld")
    'hello_world'

    >>> convert("camelCase")
    'camel_case'
    """
    result = ""

    for char in text:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char

    return result


if __name__ == "__main__":
    camelcase = input("camelCase: ")
    print(f"snake_case: {convert(camelcase)}")