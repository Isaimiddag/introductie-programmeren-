def shout(text: str) -> str:
    """
    >>> shout("hello")
    'HELLO'

    >>> shout("Who the hell put the muffins the freezer?")
    'WHO THE HELL PUT THE MUFFINS THE FREEZER?'

    >>> shout("Python 3")
    'PYTHON 3'

    >>> shout("Hallo Wereld")
    'HALLO WERELD'

    >>> shout("")
    ''
    """
    result = ""

    for char in text:
        result += char.upper()

    return result


if __name__ == "__main__":
    text = input()
    print(shout(text))